# Conditional engine recipes

## Contents

- [Selection rules](#selection-rules)
- [ECharts](#echarts)
- [GSAP](#gsap)
- [Spline](#spline)
- [Three.js](#threejs)
- [Combination rules](#combination-rules)
- [Dependency handoff](#dependency-handoff)

Versions below match `docs/UPSTREAMS.lock.json`. Recheck the lock before upgrading.

## Selection rules

| Engine | Use when | Skip when |
|---|---|---|
| ECharts | Structured data has a categorical, temporal, compositional, ranking or relationship question | Data is absent, one value is enough, or a table is clearer |
| GSAP | Motion explains hierarchy, continuity, state or a story | Motion is decorative, CSS handles it cleanly, or performance / accessibility cost is not justified |
| Spline | The user owns or supplies a Spline scene and authored 3D is central | No scene asset exists or 3D is background decoration |
| Three.js | Custom shaders, particles, geometry, camera or low-level control is essential | Spline or 2D already solves the problem |

Use `scripts/plan_artifact.py` when more than one choice is plausible.

## ECharts

Install the audited version:

```bash
npm install echarts@6.1.0
```

Prefer a modular build. Import only chart types and components the artifact uses:

```js
import * as echarts from "echarts/core";
import { BarChart, LineChart, PieChart } from "echarts/charts";
import {
  DatasetComponent,
  GridComponent,
  LegendComponent,
  TitleComponent,
  TooltipComponent,
  TransformComponent,
} from "echarts/components";
import { LabelLayout, UniversalTransition } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";

echarts.use([
  BarChart,
  LineChart,
  PieChart,
  DatasetComponent,
  GridComponent,
  LegendComponent,
  TitleComponent,
  TooltipComponent,
  TransformComponent,
  LabelLayout,
  UniversalTransition,
  CanvasRenderer,
]);
```

Build options from data and design tokens rather than hard-coded demo values:

```js
export function mountCategoryChart(element, { rows, tokens, title, unit }) {
  if (!Array.isArray(rows) || rows.length === 0) {
    element.replaceChildren(Object.assign(document.createElement("p"), {
      textContent: "暂无可用数据",
    }));
    return () => {};
  }

  const chart = echarts.init(element, null, { renderer: "canvas" });
  const option = {
    animationDuration: matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 420,
    color: tokens.chart.categorical,
    dataset: { source: [["label", "value"], ...rows.map(({ label, value }) => [label, value])] },
    title: { text: title, left: 0, textStyle: { color: tokens.color.text.primary } },
    tooltip: { trigger: "axis", valueFormatter: (value) => `${value}${unit ?? ""}` },
    grid: { left: 0, right: 16, top: 56, bottom: 8, containLabel: true },
    xAxis: { type: "category", axisLabel: { color: tokens.color.text.muted } },
    yAxis: { type: "value", axisLabel: { color: tokens.color.text.muted } },
    series: [{ type: "bar", encode: { x: "label", y: "value" }, barMaxWidth: 40 }],
  };

  chart.setOption(option);
  const resizeObserver = new ResizeObserver(() => chart.resize());
  resizeObserver.observe(element);

  return () => {
    resizeObserver.disconnect();
    chart.dispose();
  };
}
```

Chart rules:

- Put the analytical question in the title or nearby copy.
- Show units, source, time range and timezone.
- Use bar for categorical comparison, line for time, pie only for a small part-to-whole set, and table for exact lookup.
- Use `setOption` for updates; keep category identity stable so transitions track real change.
- For dynamic ranking, sort the source data on each tick, preserve item names as stable keys, show the time label, and give users pause / reduced-motion behavior.
- Use SVG renderer for crisp small static diagrams when its tradeoffs fit; use Canvas for larger / more frequently updated data.
- Provide a text summary or table for critical information.

## GSAP

Install the audited version and import only required plugins:

```bash
npm install gsap@3.15.0
```

```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);
```

Use a component-scoped context and a reduced-motion branch:

```js
export function mountSectionMotion(root) {
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reduceMotion) {
    gsap.set(root.querySelectorAll("[data-reveal]"), { clearProps: "all" });
    return () => {};
  }

  const context = gsap.context(() => {
    const timeline = gsap.timeline({
      defaults: { duration: 0.55, ease: "power2.out" },
      scrollTrigger: {
        trigger: root,
        start: "top 75%",
        once: true,
      },
    });

    timeline
      .from("[data-reveal='eyebrow']", { y: 12, autoAlpha: 0 })
      .from("[data-reveal='title']", { y: 24, autoAlpha: 0 }, "-=0.32")
      .from("[data-reveal='body']", { y: 16, autoAlpha: 0 }, "-=0.28");
  }, root);

  return () => context.revert();
}
```

Plugin-specific rules:

- **ScrollTrigger**: use for scroll-linked narrative or state, not every section. Call `refresh()` after layout-affecting media loads and kill triggers on teardown.
- **SplitText**: split only a short display line; preserve accessible text and call `revert()` when leaving the scene.
- **Flip**: use for a real layout / state transition. Capture state immediately before DOM mutation, then animate to the new layout.
- **MotionPath**: keep the path meaningful and ensure the final semantic state does not depend on seeing the animation.
- **Draggable + Inertia**: use only when direct manipulation is part of the task. Provide keyboard controls and boundaries; register Inertia only if the project license and build include it.
- **Timeline**: use labels for chapter / product states, and make interruption behavior explicit.

Do not animate height, width, top or left when transform can express the same transition. Avoid scroll hijacking. Never hide content before JavaScript is ready without a no-JS reveal path.

## Spline

Spline is an external authoring tool. Do not vendor its runtime in this MIT plugin while the runtime / viewer package metadata lacks a clear license.

Preferred input order:

1. User-provided Spline public URL or viewer export.
2. User-provided `.splinecode` plus their installed `@splinetool/runtime`.
3. User-provided downloadable code export / ZIP.

Web component pattern using the user's official export snippet:

```html
<figure class="product-scene" data-spline-shell>
  <img
    class="product-scene__poster"
    src="/assets/product-poster.webp"
    alt="产品正面与侧面外观"
    width="1600"
    height="1000"
  />
  <!-- Insert the exact <spline-viewer> and module script from the user's export here. -->
  <noscript>3D 场景需要 JavaScript；当前显示静态产品图。</noscript>
</figure>
```

Runtime pattern when the user explicitly installs the runtime:

```js
import { Application } from "@splinetool/runtime";

export async function mountSpline(canvas, sceneUrl) {
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion || !sceneUrl) return () => {};

  const app = new Application(canvas);
  await app.load(sceneUrl);

  return () => {
    // Use the cleanup method exposed by the installed runtime version.
    if (typeof app.dispose === "function") app.dispose();
  };
}
```

Keep a real `<img>` poster until the scene is ready and restore it on load failure. Core text, CTA and navigation must stay outside the scene. Do not invent a Spline URL.

## Three.js

Install the audited version:

```bash
npm install three@0.185.1
```

Use an explicit lifecycle with resize, visibility and disposal:

```js
import * as THREE from "three";

export function mountThreeScene(canvas, { poster, maxDpr = 2 } = {}) {
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced || !canvas.getContext("webgl2")) {
    if (poster) canvas.replaceWith(poster);
    return () => {};
  }

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 100);
  camera.position.set(0, 0, 5);

  const geometry = new THREE.IcosahedronGeometry(1, 3);
  const material = new THREE.MeshStandardMaterial({ color: 0x6c5ce7, roughness: 0.38 });
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh, new THREE.HemisphereLight(0xffffff, 0x202033, 2.2));

  let frame = 0;
  let visible = !document.hidden;

  const resize = () => {
    const { width, height } = canvas.getBoundingClientRect();
    renderer.setPixelRatio(Math.min(devicePixelRatio, maxDpr));
    renderer.setSize(width, height, false);
    camera.aspect = width / Math.max(height, 1);
    camera.updateProjectionMatrix();
  };

  const render = () => {
    if (!visible) return;
    mesh.rotation.y += 0.003;
    renderer.render(scene, camera);
    frame = requestAnimationFrame(render);
  };

  const onVisibility = () => {
    visible = !document.hidden;
    cancelAnimationFrame(frame);
    if (visible) render();
  };

  const observer = new ResizeObserver(resize);
  observer.observe(canvas);
  document.addEventListener("visibilitychange", onVisibility);
  resize();
  render();

  return () => {
    cancelAnimationFrame(frame);
    observer.disconnect();
    document.removeEventListener("visibilitychange", onVisibility);
    geometry.dispose();
    material.dispose();
    renderer.dispose();
  };
}
```

For production scenes, also dispose textures, render targets, controls, postprocessing passes and loaded model resources. Use `IntersectionObserver` to pause offscreen scenes. Keep DPR and texture size within the project's token budget.

## Combination rules

- ECharts + GSAP: allowed only when GSAP animates surrounding narrative or coordinates a meaningful state. Let ECharts handle its own data transition.
- Spline + GSAP: animate the surrounding DOM; use Spline's own event / variable interface for scene state. Do not fight the same transform from two runtimes.
- Three.js + GSAP: GSAP may drive camera or uniform values when a named timeline is useful; keep one render loop.
- Spline + Three.js: reject by default. Require a written reason, separate canvases and a measured performance budget.

## Dependency handoff

For every enabled engine, record:

```json
{
  "name": "echarts",
  "version": "6.1.0",
  "purpose": "Category comparison on revenue page",
  "loadMode": "npm-esm",
  "fallback": "Accessible data table",
  "license": "Apache-2.0"
}
```

Do not rely on an unpinned CDN URL in a production deliverable. If a no-build single HTML artifact uses a CDN, pin the exact version, document network dependence and provide a local or static fallback.
