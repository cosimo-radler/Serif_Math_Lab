from pathlib import Path


ORIGINAL = Path("/Users/cosimoradler/Documents/Codex/2026-06-02/files-mentioned-by-the-user-index/outputs/index_2_original_backup.html")
SRC = ORIGINAL if ORIGINAL.exists() else Path("/Users/cosimoradler/Downloads/index_2.html")
OUT = Path("/Users/cosimoradler/Documents/Codex/2026-06-02/files-mentioned-by-the-user-index/outputs/index_2_enhanced.html")


LAB_CSS = r'''

/* expanded math labs */
.lab-stack{display:grid;gap:5.5rem;margin-top:2.8rem;}
.lab{border-top:1px solid var(--line);padding-top:3.2rem;}
.lab:first-child{border-top:0;padding-top:0;}
.lab-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(260px,0.78fr);gap:28px;align-items:start;margin-bottom:1.6rem;}
.lab h3{font-weight:300;font-size:clamp(1.45rem,2.4vw,2rem);margin:0 0 0.65rem;letter-spacing:0;}
.lab .one{font-size:1rem;color:var(--mut);margin:0;font-weight:300;line-height:1.6;}
.lab .ceq{overflow-x:auto;font-size:0.92em;color:var(--ink);}
.lab .ceq::-webkit-scrollbar{height:4px;}.lab .ceq::-webkit-scrollbar-thumb{background:var(--mut2);}
.lab-stage{display:grid;grid-template-columns:minmax(280px,1fr) 220px;gap:22px;align-items:start;margin:1.4rem 0 1.4rem;}
.lab-stage canvas,.three-stage{width:100%;aspect-ratio:1/1;border:1px solid var(--line);background:var(--bg);display:block;touch-action:none;}
.three-stage{position:relative;overflow:hidden;}
.three-stage canvas{border:0;aspect-ratio:auto;}
.three-fallback{position:absolute;inset:0;display:grid;place-items:center;padding:24px;text-align:center;color:var(--mut);font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:0.1em;text-transform:uppercase;}
.readout{display:grid;gap:10px;border:1px solid var(--line);padding:16px;min-height:100%;}
.readout .over{font-size:10px;}
.readout p{font-family:"IBM Plex Mono",monospace;font-size:11px;line-height:1.55;letter-spacing:0.06em;color:var(--mut);margin:0;}
.lab .actions{margin-top:0.8rem;}
.lab .controls{margin-bottom:1.2rem;}
.lab .controls{grid-template-columns:repeat(auto-fit,minmax(280px,1fr));}
@media(max-width:760px){.lab-top,.lab-stage{grid-template-columns:1fr}.readout{min-height:auto}}
'''


LAB_HTML = r'''
<!-- 05 -->
<section>
  <div class="head"><span class="num">05</span><h2>The expanded equation lab</h2></div>
  <p class="desc">Every system below is live. Some are ideal skeletons, some are fields, some are physical instabilities. The useful curves can be handed back to the brush in 04, so the mathematics can become residue.</p>

  <div class="lab-stack">

    <article class="lab" id="lab-elastica-wrap">
      <div class="lab-top">
        <div><h3>Euler&#8217;s elastica</h3><p class="one">A bent bristle solves the same differential equation as a pendulum. Raise the load and the line buckles from quiet arc into stored tension.</p></div>
        <div class="ceq">\( \theta''(s)=-\lambda\sin\theta,\quad \mathbf{x}'(s)=(\cos\theta,\sin\theta) \)</div>
      </div>
      <div class="lab-stage"><canvas id="lab-elastica"></canvas><div class="readout"><div class="over">what to watch</div><p id="lab-elastica-note">Curvature concentrates where the imaginary bristle stores energy.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>load</label><input id="el-load" type="range" min="4" max="48" step="0.5" value="26"><span class="val" id="el-loado">26.0</span></div>
        <div class="ctl"><label>start</label><input id="el-start" type="range" min="0.4" max="3.1" step="0.01" value="2.45"><span class="val" id="el-starto">2.45</span></div>
        <div class="ctl"><label>length</label><input id="el-len" type="range" min="180" max="900" step="10" value="520"><span class="val" id="el-leno">520</span></div>
      </div>
      <div class="actions"><button id="el-play">play bend</button><button id="el-rand">random bend</button><button id="el-brush">brush this</button><button id="el-dl">save png</button></div>
    </article>

    <article class="lab" id="lab-dejong-wrap">
      <div class="lab-top">
        <div><h3>de Jong attractor</h3><p class="one">Four parameters fold the plane into smoke. Tiny shifts move it from torn cloth to orchid to dust storm.</p></div>
        <div class="ceq">\( x'=\sin(ay)-\cos(bx),\quad y'=\sin(cx)-\cos(dy) \)</div>
      </div>
      <div class="lab-stage"><canvas id="lab-dejong"></canvas><div class="readout"><div class="over">orbit density</div><p id="dj-note">Iterate one point long enough and probability becomes drawing.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>a</label><input id="dj-a" type="range" min="-3" max="3" step="0.01" value="-2.0"><span class="val" id="dj-ao">-2.00</span></div>
        <div class="ctl"><label>b</label><input id="dj-b" type="range" min="-3" max="3" step="0.01" value="-2.0"><span class="val" id="dj-bo">-2.00</span></div>
        <div class="ctl"><label>c</label><input id="dj-c" type="range" min="-3" max="3" step="0.01" value="-1.2"><span class="val" id="dj-co">-1.20</span></div>
        <div class="ctl"><label>d</label><input id="dj-d" type="range" min="-3" max="3" step="0.01" value="2.0"><span class="val" id="dj-do">2.00</span></div>
      </div>
      <div class="actions"><button id="dj-play">play drift</button><button id="dj-rand">random attractor</button><button id="dj-dl">save png</button></div>
    </article>

    <article class="lab" id="lab-liss-wrap">
      <div class="lab-top">
        <div><h3>Lissajous</h3><p class="one">The harmonograph before friction: pure phase, pure ratio, no decay. Rational ratios close; irrational-feeling ones wander.</p></div>
        <div class="ceq">\( x=\sin(at),\quad y=\sin(bt+\delta) \)</div>
      </div>
      <div class="lab-stage"><canvas id="lab-liss"></canvas><div class="readout"><div class="over">closure</div><p id="li-note">The curve closes when the frequency ratio finds a small integer agreement.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>a</label><input id="li-a" type="range" min="1" max="12" step="1" value="3"><span class="val" id="li-ao">3</span></div>
        <div class="ctl"><label>b</label><input id="li-b" type="range" min="1" max="12" step="1" value="2"><span class="val" id="li-bo">2</span></div>
        <div class="ctl"><label>phase</label><input id="li-ph" type="range" min="0" max="6.283" step="0.01" value="1.57"><span class="val" id="li-pho">1.57</span></div>
      </div>
      <div class="actions"><button id="li-play">play phase</button><button id="li-rand">random ratio</button><button id="li-brush">brush this</button><button id="li-dl">save png</button></div>
    </article>

    <article class="lab" id="lab-hypo-wrap">
      <div class="lab-top">
        <div><h3>Hypotrochoid</h3><p class="one">A point attached to a circle rolling inside another circle. The visible lace is a record of hidden gearing.</p></div>
        <div class="ceq">\( x=(R-r)\cos\theta+d\cos\frac{R-r}{r}\theta,\quad y=(R-r)\sin\theta-d\sin\frac{R-r}{r}\theta \)</div>
      </div>
      <div class="lab-stage"><canvas id="lab-hypo"></canvas><div class="readout"><div class="over">mechanism</div><p id="hy-note">Integer-like gear ratios make petals; offsets pull the pen away from the rolling center.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>R</label><input id="hy-R" type="range" min="3" max="12" step="1" value="8"><span class="val" id="hy-Ro">8</span></div>
        <div class="ctl"><label>r</label><input id="hy-r" type="range" min="1" max="8" step="1" value="3"><span class="val" id="hy-ro">3</span></div>
        <div class="ctl"><label>d</label><input id="hy-d" type="range" min="1" max="12" step="0.1" value="5"><span class="val" id="hy-do">5.0</span></div>
        <div class="ctl"><label>turns</label><input id="hy-turns" type="range" min="1" max="18" step="1" value="8"><span class="val" id="hy-turnso">8</span></div>
      </div>
      <div class="actions"><button id="hy-play">play gear</button><button id="hy-rand">random gear</button><button id="hy-brush">brush this</button><button id="hy-dl">save png</button></div>
    </article>

    <article class="lab" id="lab-phyllo-wrap">
      <div class="lab-top">
        <div><h3>Phyllotaxis</h3><p class="one">The golden angle is a refusal to line up. Change it by a degree and nature&#8217;s packing turns into spokes.</p></div>
        <div class="ceq">\( r=c\sqrt{n},\quad \theta=n\alpha \)</div>
      </div>
      <div class="lab-stage"><div class="three-stage" id="phy-3d"></div><div class="readout"><div class="over">2D to shell</div><p id="ph-note">The same index can pack a disk or climb a spherical shell.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>angle</label><input id="ph-ang" type="range" min="120" max="150" step="0.01" value="137.507"><span class="val" id="ph-ango">137.51</span></div>
        <div class="ctl"><label>count</label><input id="ph-count" type="range" min="120" max="1600" step="20" value="720"><span class="val" id="ph-counto">720</span></div>
        <div class="ctl"><label>shell</label><input id="ph-shell" type="range" min="0" max="1" step="0.01" value="0.65"><span class="val" id="ph-shello">0.65</span></div>
      </div>
      <div class="actions"><button id="ph-golden">golden angle</button><button id="ph-brush">brush spiral</button></div>
    </article>

    <article class="lab" id="lab-chladni-wrap">
      <div class="lab-top">
        <div><h3>Chladni figures</h3><p class="one">Sound made visible. The bright lines are where a vibrating plate refuses to move, so sand has a place to settle.</p></div>
        <div class="ceq">\( \cos(n\pi x)\cos(m\pi y)-\cos(m\pi x)\cos(n\pi y)=0 \)</div>
      </div>
      <div class="lab-stage"><div class="three-stage" id="ch-3d"></div><div class="readout"><div class="over">nodes</div><p id="ch-note">The 3D surface shows displacement; the pale ridges are the near-zero nodal set.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>n</label><input id="ch-n" type="range" min="1" max="12" step="1" value="4"><span class="val" id="ch-no">4</span></div>
        <div class="ctl"><label>m</label><input id="ch-m" type="range" min="1" max="12" step="1" value="3"><span class="val" id="ch-mo">3</span></div>
        <div class="ctl"><label>height</label><input id="ch-height" type="range" min="0" max="1.4" step="0.05" value="0.65"><span class="val" id="ch-heighto">0.65</span></div>
      </div>
      <div class="actions"><button id="ch-play">play modes</button><button id="ch-swap">swap modes</button><button id="ch-rand">random plate</button></div>
    </article>

    <article class="lab" id="lab-rd-wrap">
      <div class="lab-top">
        <div><h3>Reaction&#8211;diffusion</h3><p class="one">Two chemicals chase each other through a grid. Feed and kill rates decide whether the page grows spots, worms, or scar tissue.</p></div>
        <div class="ceq">\[ \partial_t u=D_u\nabla^2u-uv^2+f(1-u),\quad \partial_t v=D_v\nabla^2v+uv^2-(f+k)v \]</div>
      </div>
      <div class="lab-stage"><canvas id="lab-rd"></canvas><div class="readout"><div class="over">gray-scott</div><p id="rd-note">Pause on an interesting instability, then save the field as texture.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>feed</label><input id="rd-f" type="range" min="0.01" max="0.08" step="0.001" value="0.036"><span class="val" id="rd-fo">0.036</span></div>
        <div class="ctl"><label>kill</label><input id="rd-k" type="range" min="0.035" max="0.075" step="0.001" value="0.060"><span class="val" id="rd-ko">0.060</span></div>
        <div class="ctl"><label>scale</label><input id="rd-scale" type="range" min="0.5" max="1.8" step="0.05" value="1.0"><span class="val" id="rd-scaleo">1.00</span></div>
      </div>
      <div class="actions"><button id="rd-pause">pause</button><button id="rd-seed">seed</button><button id="rd-dl">save png</button></div>
    </article>

    <article class="lab" id="lab-torus-wrap">
      <div class="lab-top">
        <div><h3>Torus projection</h3><p class="one">A ring seen from a chosen angle. Projection turns one continuous surface into loops, twins, and apparent crossings.</p></div>
        <div class="ceq">\[ \mathbf{X}=((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v),\quad (X,Y)\mapsto\frac{(X,Y)}{d-Z} \]</div>
      </div>
      <div class="lab-stage"><div class="three-stage" id="tor-3d"></div><div class="readout"><div class="over">projection</div><p id="tor-note">Drag to rotate. Pull distance down and perspective turns topology into a mark.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>tube</label><input id="tor-tube" type="range" min="0.12" max="0.65" step="0.01" value="0.36"><span class="val" id="tor-tubeo">0.36</span></div>
        <div class="ctl"><label>twist</label><input id="tor-twist" type="range" min="0" max="8" step="1" value="2"><span class="val" id="tor-twisto">2</span></div>
        <div class="ctl"><label>auto</label><input id="tor-auto" type="range" min="0" max="1" step="1" value="1"><span class="val" id="tor-autoo">1</span></div>
      </div>
      <div class="actions"><button id="tor-play">play twist</button></div>
    </article>

    <article class="lab" id="lab-lorenz-wrap">
      <div class="lab-top">
        <div><h3>Lorenz attractor</h3><p class="one">A fluid-convection model that became the emblem of chaos. The butterfly is not metaphorical; it is phase space folding.</p></div>
        <div class="ceq">\( \dot{x}=\sigma(y-x),\quad \dot{y}=x(\rho-z)-y,\quad \dot{z}=xy-\beta z \)</div>
      </div>
      <div class="lab-stage"><div class="three-stage" id="lor-3d"></div><div class="readout"><div class="over">sensitive dependence</div><p id="lor-note">Two nearby states share a wing, then disagree completely.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>sigma</label><input id="lor-s" type="range" min="4" max="18" step="0.1" value="10"><span class="val" id="lor-so">10.0</span></div>
        <div class="ctl"><label>rho</label><input id="lor-r" type="range" min="10" max="48" step="0.1" value="28"><span class="val" id="lor-ro">28.0</span></div>
        <div class="ctl"><label>beta</label><input id="lor-b" type="range" min="1.5" max="4" step="0.01" value="2.67"><span class="val" id="lor-bo">2.67</span></div>
        <div class="ctl"><label>trail</label><input id="lor-trail" type="range" min="1800" max="8200" step="200" value="5200"><span class="val" id="lor-trailo">5200</span></div>
      </div>
      <div class="actions"><button id="lor-play">play weather</button><button id="lor-reset">reset trail</button><button id="lor-brush">brush projection</button></div>
    </article>

    <article class="lab" id="lab-rossler-wrap">
      <div class="lab-top">
        <div><h3>Rössler attractor</h3><p class="one">A spiral that keeps almost closing, then folds upward and escapes. It feels calmer than Lorenz until it slips.</p></div>
        <div class="ceq">\( \dot{x}=-(y+z),\quad \dot{y}=x+ay,\quad \dot{z}=b+z(x-c) \)</div>
      </div>
      <div class="lab-stage"><div class="three-stage" id="ros-3d"></div><div class="readout"><div class="over">spiral fold</div><p id="ros-note">Most of the orbit is a slow sheet; the fold injects surprise back into it.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>a</label><input id="ros-a" type="range" min="0.05" max="0.45" step="0.01" value="0.20"><span class="val" id="ros-ao">0.20</span></div>
        <div class="ctl"><label>b</label><input id="ros-b" type="range" min="0.05" max="0.45" step="0.01" value="0.20"><span class="val" id="ros-bo">0.20</span></div>
        <div class="ctl"><label>c</label><input id="ros-c" type="range" min="3" max="10" step="0.1" value="5.7"><span class="val" id="ros-co">5.7</span></div>
        <div class="ctl"><label>trail</label><input id="ros-trail" type="range" min="1800" max="8200" step="200" value="5200"><span class="val" id="ros-trailo">5200</span></div>
      </div>
      <div class="actions"><button id="ros-play">play fold</button><button id="ros-reset">reset trail</button><button id="ros-brush">brush projection</button></div>
    </article>

    <article class="lab" id="lab-thomas-wrap">
      <div class="lab-top">
        <div><h3>Thomas attractor</h3><p class="one">A cyclic system: each axis is driven by the sine of another and damped by itself. The result is a knot of soft turbulence.</p></div>
        <div class="ceq">\( \dot{x}=\sin y-bx,\quad \dot{y}=\sin z-by,\quad \dot{z}=\sin x-bz \)</div>
      </div>
      <div class="lab-stage"><div class="three-stage" id="tho-3d"></div><div class="readout"><div class="over">cyclic drift</div><p id="tho-note">Lower damping lets the orbit swell; higher damping tightens the knot.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>b</label><input id="tho-b" type="range" min="0.12" max="0.35" step="0.005" value="0.19"><span class="val" id="tho-bo">0.190</span></div>
        <div class="ctl"><label>trail</label><input id="tho-trail" type="range" min="800" max="6200" step="100" value="3600"><span class="val" id="tho-trailo">3600</span></div>
      </div>
      <div class="actions"><button id="tho-play">play damping</button><button id="tho-reset">reset trail</button><button id="tho-brush">brush projection</button></div>
    </article>

    <article class="lab" id="lab-wave-wrap">
      <div class="lab-top">
        <div><h3>Wave interference</h3><p class="one">Two emitters write phase into the same surface. Drag the sources and watch constructive and destructive agreement move through the field.</p></div>
        <div class="ceq">\( A(x,y,t)=\sum_i \frac{\sin(k\|p-p_i\|-\omega t+\phi_i)}{1+d\|p-p_i\|} \)</div>
      </div>
      <div class="lab-stage"><div class="three-stage" id="wav-3d"></div><div class="readout"><div class="over">drag sources</div><p id="wav-note">The surface is the field amplitude; the pale lines are moments of agreement.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>wave</label><input id="wav-len" type="range" min="0.12" max="0.8" step="0.01" value="0.32"><span class="val" id="wav-leno">0.32</span></div>
        <div class="ctl"><label>phase</label><input id="wav-phase" type="range" min="0" max="6.283" step="0.01" value="1.8"><span class="val" id="wav-phaseo">1.80</span></div>
        <div class="ctl"><label>height</label><input id="wav-height" type="range" min="0.1" max="1.4" step="0.05" value="0.7"><span class="val" id="wav-heighto">0.70</span></div>
      </div>
      <div class="actions"><button id="wav-play">play waves</button><button id="wav-reset">reset emitters</button></div>
    </article>

    <article class="lab" id="lab-field-wrap">
      <div class="lab-top">
        <div><h3>Magnetic / vector field</h3><p class="one">Poles do not draw lines; they define a direction at every point. The field lines are just particles obeying local instruction.</p></div>
        <div class="ceq">\( \mathbf{F}(p)=\sum_i q_i\frac{p-p_i}{\|p-p_i\|^3} \)</div>
      </div>
      <div class="lab-stage"><canvas id="lab-field"></canvas><div class="readout"><div class="over">field lines</div><p id="vf-note">Drag a pole. Reverse charge and the whole page changes its arrows.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>strength</label><input id="vf-strength" type="range" min="0.2" max="2.8" step="0.05" value="1.1"><span class="val" id="vf-strengtho">1.10</span></div>
        <div class="ctl"><label>lines</label><input id="vf-lines" type="range" min="20" max="120" step="4" value="64"><span class="val" id="vf-lineso">64</span></div>
      </div>
      <div class="actions"><button id="vf-play">play poles</button><button id="vf-flip">flip charge</button><button id="vf-reset">reset poles</button><button id="vf-dl">save png</button></div>
    </article>

    <article class="lab" id="lab-vortex-wrap">
      <div class="lab-top">
        <div><h3>Vorticity flow</h3><p class="one">Particles reveal an invisible incompressible flow. Swirl makes loops; diffusion lets the trace breathe outward.</p></div>
        <div class="ceq">\( \dot{p}=\nabla^\perp \psi(p,t),\quad \nabla^\perp\psi=(\partial_y\psi,-\partial_x\psi) \)</div>
      </div>
      <div class="lab-stage"><canvas id="lab-vortex"></canvas><div class="readout"><div class="over">curl field</div><p id="vo-note">The particles are not the fluid; they are the handwriting that lets you see it.</p></div></div>
      <div class="controls">
        <div class="ctl"><label>swirl</label><input id="vo-swirl" type="range" min="0.2" max="3" step="0.05" value="1.35"><span class="val" id="vo-swirlo">1.35</span></div>
        <div class="ctl"><label>diffuse</label><input id="vo-diff" type="range" min="0" max="0.08" step="0.005" value="0.02"><span class="val" id="vo-diffo">0.020</span></div>
        <div class="ctl"><label>particles</label><input id="vo-count" type="range" min="300" max="2400" step="100" value="1200"><span class="val" id="vo-counto">1200</span></div>
      </div>
      <div class="actions"><button id="vo-pause">pause</button><button id="vo-reset">reset flow</button><button id="vo-dl">save png</button></div>
    </article>

  </div>
</section>
'''


LAB_JS = r'''
<script type="module">
import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js";

const I=[242,239,232], TAU=Math.PI*2;
const $id=id=>document.getElementById(id);
const val=id=>+$id(id).value;
const fmt=(id,n=2)=>{ const el=$id(id), out=$id(id+"o"); if(out) out.textContent=(+el.value).toFixed(n); };
const ink=a=>`rgba(${I[0]},${I[1]},${I[2]},${a})`;

function visible(el, on){
  const io=new IntersectionObserver(es=>es.forEach(e=>on(e.isIntersecting)),{threshold:0.04});
  io.observe(el);
}
function sizeCanvas(cv, ratio=1){
  const dpr=Math.min(2,window.devicePixelRatio||1), w=Math.max(280,cv.clientWidth||520), h=Math.round(w*ratio);
  const pw=Math.round(w*dpr), ph=Math.round(h*dpr);
  if(cv.width!==pw||cv.height!==ph){ cv.width=pw; cv.height=ph; }
  cv.style.height=h+"px";
  const ctx=cv.getContext("2d"); ctx.setTransform(dpr,0,0,dpr,0,0); return {ctx,w,h,dpr};
}
function fitPts(pts,w,h,pad){
  let mnx=1e9,mny=1e9,mxx=-1e9,mxy=-1e9;
  for(const p of pts){ if(p[0]<mnx)mnx=p[0]; if(p[0]>mxx)mxx=p[0]; if(p[1]<mny)mny=p[1]; if(p[1]>mxy)mxy=p[1]; }
  const s=Math.min((w-2*pad)/((mxx-mnx)||1),(h-2*pad)/((mxy-mny)||1));
  return pts.map(p=>[(w-(mxx-mnx)*s)/2+(p[0]-mnx)*s,(h-(mxy-mny)*s)/2+(p[1]-mny)*s]);
}
function drawPath(cv, pts, lw=1.4){
  const {ctx,w,h}=sizeCanvas(cv);
  ctx.fillStyle="#000"; ctx.fillRect(0,0,w,h);
  const p=fitPts(pts,w,h,Math.min(w,h)*0.11);
  ctx.strokeStyle=ink(0.78); ctx.lineWidth=lw; ctx.lineJoin="round"; ctx.lineCap="round";
  ctx.beginPath(); ctx.moveTo(p[0][0],p[0][1]); for(let i=1;i<p.length;i++) ctx.lineTo(p[i][0],p[i][1]); ctx.stroke();
}
function dlCanvas(cv,name){ download(cv.toDataURL("image/png"),name); }
function sendBrush(label, pts){
  window.serifBrushPath=pts.map(p=>[p[0],p[1]]);
  const sel=$id("br-curve");
  if(sel){
    let opt=[...sel.options].find(o=>o.value==="custom");
    if(!opt){ opt=document.createElement("option"); opt.value="custom"; sel.appendChild(opt); }
    opt.textContent=label; sel.value="custom";
  }
  $id("br-render")?.click();
  $id("br-cv")?.scrollIntoView({behavior:"smooth",block:"center"});
}
function bindInputs(ids, draw, digits=2){ ids.forEach(id=>$id(id)?.addEventListener("input",()=>{fmt(id,digits); draw();})); }
function setCtl(id,v,d=2){
  const e=$id(id); if(!e) return;
  const mn=+e.min, mx=+e.max, step=e.step==="1"?0:d;
  e.value=Math.max(mn,Math.min(mx,v)).toFixed(step);
  fmt(id,step);
}
function motionButton(id, activeText, fn, onToggle){
  const b=$id(id); if(!b) return ()=>false;
  const idleText=b.textContent; let run=false,last=0;
  function tick(now){
    if(!run) return;
    const dt=Math.min(0.08,(now-last)/1000||0.016); last=now;
    fn(now*0.001,dt);
    requestAnimationFrame(tick);
  }
  b.onclick=()=>{
    run=!run;
    b.textContent=run?activeText:idleText;
    if(onToggle) onToggle(run);
    if(run){ last=performance.now(); fn(last*0.001,0.016); requestAnimationFrame(tick); }
  };
  return ()=>run;
}

function elasticaLab(){
  const cv=$id("lab-elastica"); if(!cv) return; let last=[];
  function pts(){
    const n=val("el-len")|0, load=val("el-load"), th0=val("el-start"); let th=th0,w=0,x=0,y=0; const a=[];
    for(let i=0;i<n;i++){ const ds=1/n; w+=-load*Math.sin(th)*ds; th+=w*ds; x+=Math.cos(th)*ds; y+=Math.sin(th)*ds; a.push([x,y]); }
    return a;
  }
  function draw(){ ["el-load","el-start"].forEach(id=>fmt(id, id==="el-load"?1:2)); fmt("el-len",0); last=pts(); drawPath(cv,last,2.2); }
  bindInputs(["el-load","el-start","el-len"],draw);
  motionButton("el-play","stop bend",t=>{ setCtl("el-load",24+16*Math.sin(t*0.9),1); setCtl("el-start",1.75+0.85*Math.sin(t*0.63+1.2),2); draw(); });
  $id("el-rand").onclick=()=>{ $id("el-load").value=(8+Math.random()*38).toFixed(1); $id("el-start").value=(0.7+Math.random()*2.2).toFixed(2); draw(); };
  $id("el-brush").onclick=()=>sendBrush("custom elastica",last);
  $id("el-dl").onclick=()=>dlCanvas(cv,"serif_elastica.png");
  window.addEventListener("resize",draw); draw();
}

function deJongLab(){
  const cv=$id("lab-dejong"); if(!cv) return;
  function draw(){
    ["dj-a","dj-b","dj-c","dj-d"].forEach(id=>fmt(id,2));
    const {ctx,w,h}=sizeCanvas(cv), W=cv.width, H=cv.height, dens=new Float32Array(W*H);
    let x=0.1,y=0.1,mx=1,a=val("dj-a"),b=val("dj-b"),c=val("dj-c"),d=val("dj-d");
    for(let i=0;i<260000;i++){ const xn=Math.sin(a*y)-Math.cos(b*x), yn=Math.sin(c*x)-Math.cos(d*y); x=xn;y=yn;
      if(i>40){ const px=((x+2.3)/4.6*(W-1))|0, py=((y+2.3)/4.6*(H-1))|0; if(px>=0&&px<W&&py>=0&&py<H){ const v=++dens[py*W+px]; if(v>mx)mx=v; } }
    }
    const img=ctx.createImageData(W,H), bf=img.data, lm=Math.log(1+mx);
    for(let i=0;i<W*H;i++){ const L=Math.pow(Math.log(1+dens[i])/lm,0.62), j=i*4, cc=L*255; bf[j]=I[0]/255*cc; bf[j+1]=I[1]/255*cc; bf[j+2]=I[2]/255*cc; bf[j+3]=255; }
    ctx.setTransform(1,0,0,1,0,0); ctx.putImageData(img,0,0); ctx.setTransform((window.devicePixelRatio||1),0,0,(window.devicePixelRatio||1),0,0);
  }
  bindInputs(["dj-a","dj-b","dj-c","dj-d"],draw);
  let djLast=0; motionButton("dj-play","stop drift",t=>{ if(t-djLast<0.18) return; djLast=t; setCtl("dj-a",-1.8+0.9*Math.sin(t*0.31),2); setCtl("dj-b",-2.0+0.85*Math.sin(t*0.27+1.5),2); setCtl("dj-c",-1.2+0.75*Math.sin(t*0.23+2.1),2); setCtl("dj-d",2.0+0.7*Math.sin(t*0.29+0.4),2); draw(); });
  $id("dj-rand").onclick=()=>{ ["dj-a","dj-b","dj-c","dj-d"].forEach(id=>$id(id).value=(Math.random()*6-3).toFixed(2)); draw(); };
  $id("dj-dl").onclick=()=>dlCanvas(cv,"serif_dejong.png");
  window.addEventListener("resize",draw); draw();
}

function lissLab(){
  const cv=$id("lab-liss"); if(!cv) return; let last=[];
  function make(){ const n=2600,a=val("li-a"),b=val("li-b"),ph=val("li-ph"), pts=[]; for(let i=0;i<n;i++){ const t=TAU*4*i/(n-1); pts.push([Math.sin(a*t),Math.sin(b*t+ph)]); } return pts; }
  function draw(){ fmt("li-a",0); fmt("li-b",0); fmt("li-ph",2); last=make(); drawPath(cv,last,1.4); }
  bindInputs(["li-a","li-b","li-ph"],draw);
  motionButton("li-play","stop phase",t=>{ setCtl("li-ph",(t*0.85)%TAU,2); draw(); });
  $id("li-rand").onclick=()=>{ $id("li-a").value=1+(Math.random()*10|0); $id("li-b").value=1+(Math.random()*10|0); $id("li-ph").value=(Math.random()*TAU).toFixed(2); draw(); };
  $id("li-brush").onclick=()=>sendBrush("custom lissajous",last);
  $id("li-dl").onclick=()=>dlCanvas(cv,"serif_lissajous.png");
  window.addEventListener("resize",draw); draw();
}

function hypoLab(){
  const cv=$id("lab-hypo"); if(!cv) return; let last=[];
  function make(){ const R=val("hy-R"),r=Math.min(val("hy-r"),R-0.4),d=val("hy-d"),turns=val("hy-turns"),n=3600,pts=[]; for(let i=0;i<n;i++){ const t=TAU*turns*i/(n-1); pts.push([(R-r)*Math.cos(t)+d*Math.cos((R-r)/r*t),(R-r)*Math.sin(t)-d*Math.sin((R-r)/r*t)]); } return pts; }
  function draw(){ ["hy-R","hy-r","hy-turns"].forEach(id=>fmt(id,0)); fmt("hy-d",1); last=make(); drawPath(cv,last,1.35); }
  bindInputs(["hy-R","hy-r","hy-d","hy-turns"],draw);
  let hyLast=0; motionButton("hy-play","stop gear",t=>{ if(t-hyLast<0.09) return; hyLast=t; setCtl("hy-d",5.8+3.2*Math.sin(t*0.7),1); setCtl("hy-turns",7+3*Math.sin(t*0.37+0.5),0); draw(); });
  $id("hy-rand").onclick=()=>{ $id("hy-R").value=4+(Math.random()*8|0); $id("hy-r").value=1+(Math.random()*5|0); $id("hy-d").value=(1+Math.random()*10).toFixed(1); draw(); };
  $id("hy-brush").onclick=()=>sendBrush("custom hypotrochoid",last);
  $id("hy-dl").onclick=()=>dlCanvas(cv,"serif_hypotrochoid.png");
  window.addEventListener("resize",draw); draw();
}

function rdLab(){
  const cv=$id("lab-rd"); if(!cv) return; const N=120; let u,v,u2,v2,run=true,active=false,raf=0;
  function seed(){ u=new Float32Array(N*N).fill(1); v=new Float32Array(N*N); u2=new Float32Array(N*N); v2=new Float32Array(N*N); for(let y=48;y<72;y++)for(let x=48;x<72;x++){ v[y*N+x]=0.9; u[y*N+x]=0.25; } for(let i=0;i<900;i++){ const x=(Math.random()*N)|0,y=(Math.random()*N)|0; v[y*N+x]=Math.random(); } }
  function lap(A,x,y){ const xm=(x+N-1)%N,xp=(x+1)%N,ym=(y+N-1)%N,yp=(y+1)%N; return A[y*N+x]*-1+A[y*N+xm]*0.2+A[y*N+xp]*0.2+A[ym*N+x]*0.2+A[yp*N+x]*0.2+A[ym*N+xm]*0.05+A[ym*N+xp]*0.05+A[yp*N+xm]*0.05+A[yp*N+xp]*0.05; }
  function step(){ const f=val("rd-f"),k=val("rd-k"),sc=val("rd-scale"),du=0.16*sc,dv=0.08*sc; for(let y=0;y<N;y++)for(let x=0;x<N;x++){ const i=y*N+x,U=u[i],V=v[i],uvv=U*V*V; u2[i]=U+(du*lap(u,x,y)-uvv+f*(1-U)); v2[i]=V+(dv*lap(v,x,y)+uvv-(f+k)*V); } [u,u2]=[u2,u]; [v,v2]=[v2,v]; }
  function paint(){ ["rd-f","rd-k"].forEach(id=>fmt(id,3)); fmt("rd-scale",2); const {ctx,w,h}=sizeCanvas(cv), img=ctx.createImageData(N,N), bf=img.data; for(let i=0;i<N*N;i++){ const L=Math.max(0,Math.min(1,(v[i]-u[i]*0.18)*1.8+0.1)), j=i*4, cc=L*255; bf[j]=I[0]/255*cc; bf[j+1]=I[1]/255*cc; bf[j+2]=I[2]/255*cc; bf[j+3]=255; } const off=document.createElement("canvas"); off.width=N; off.height=N; off.getContext("2d").putImageData(img,0,0); ctx.imageSmoothingEnabled=false; ctx.drawImage(off,0,0,w,h); }
  function loop(){ if(active&&run){ for(let i=0;i<5;i++) step(); paint(); } raf=requestAnimationFrame(loop); }
  bindInputs(["rd-f","rd-k","rd-scale"],paint,3);
  $id("rd-pause").onclick=()=>{ run=!run; $id("rd-pause").textContent=run?"pause":"play"; };
  $id("rd-seed").onclick=()=>{ seed(); paint(); };
  $id("rd-dl").onclick=()=>dlCanvas(cv,"serif_reaction_diffusion.png");
  seed(); visible(cv,vv=>active=vv); loop();
}

function fieldLab(){
  const cv=$id("lab-field"); if(!cv) return; let poles=[{x:.34,y:.5,q:1},{x:.66,y:.5,q:-1}], drag=-1;
  function F(x,y){ let fx=0,fy=0; for(const p of poles){ const dx=x-p.x,dy=y-p.y,r2=dx*dx+dy*dy+0.002, s=p.q*val("vf-strength")/(r2*Math.sqrt(r2)); fx+=dx*s; fy+=dy*s; } return [fx,fy]; }
  function draw(){ fmt("vf-strength",2); fmt("vf-lines",0); const {ctx,w,h}=sizeCanvas(cv); ctx.fillStyle="#000";ctx.fillRect(0,0,w,h); ctx.lineWidth=0.8; ctx.strokeStyle=ink(0.38); const lines=val("vf-lines")|0; for(let i=0;i<lines;i++){ const p=poles[i%poles.length], a=TAU*i/lines, dir=p.q>0?1:-1; let x=p.x+Math.cos(a)*0.035,y=p.y+Math.sin(a)*0.035; ctx.beginPath(); ctx.moveTo(x*w,y*h); for(let s=0;s<260;s++){ const f=F(x,y), m=Math.hypot(f[0],f[1])||1; x+=dir*f[0]/m*0.007; y+=dir*f[1]/m*0.007; if(x<0||x>1||y<0||y>1) break; ctx.lineTo(x*w,y*h); } ctx.stroke(); }
    for(const p of poles){ ctx.fillStyle=p.q>0?ink(0.95):"rgba(242,239,232,0.18)"; ctx.beginPath(); ctx.arc(p.x*w,p.y*h,12,0,TAU); ctx.fill(); ctx.strokeStyle=ink(0.9); ctx.stroke(); }
  }
  cv.addEventListener("pointerdown",e=>{ const r=cv.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height; drag=poles.findIndex(p=>Math.hypot(p.x-x,p.y-y)<0.08); });
  cv.addEventListener("pointermove",e=>{ if(drag<0) return; const r=cv.getBoundingClientRect(); poles[drag].x=Math.max(.05,Math.min(.95,(e.clientX-r.left)/r.width)); poles[drag].y=Math.max(.05,Math.min(.95,(e.clientY-r.top)/r.height)); draw(); });
  window.addEventListener("pointerup",()=>drag=-1);
  bindInputs(["vf-strength","vf-lines"],draw);
  let vfLast=0; motionButton("vf-play","stop poles",t=>{ if(t-vfLast<0.05) return; vfLast=t; poles[0].x=.33+.12*Math.sin(t*.7); poles[0].y=.5+.16*Math.cos(t*.53); poles[1].x=.67+.12*Math.sin(t*.61+2); poles[1].y=.5+.16*Math.cos(t*.47+1); draw(); });
  $id("vf-flip").onclick=()=>{ poles[1].q*=-1; draw(); };
  $id("vf-reset").onclick=()=>{ poles=[{x:.34,y:.5,q:1},{x:.66,y:.5,q:-1}]; draw(); };
  $id("vf-dl").onclick=()=>dlCanvas(cv,"serif_vector_field.png");
  window.addEventListener("resize",draw); draw();
}

function vortexLab(){
  const cv=$id("lab-vortex"); if(!cv) return; let pts=[],run=true,active=false,raf=0,t=0;
  function reset(){ const n=val("vo-count")|0; pts=Array.from({length:n},()=>[Math.random(),Math.random()]); const {ctx,w,h}=sizeCanvas(cv); ctx.fillStyle="#000"; ctx.fillRect(0,0,w,h); }
  function flow(x,y){ const s=val("vo-swirl"); const a=Math.sin(TAU*(y*1.7+t*.08))+0.5*Math.sin(TAU*(x+y+t*.05)); const b=Math.cos(TAU*(x*1.4-t*.06))-0.5*Math.cos(TAU*(x-y)); return [s*a,s*b]; }
  function step(){ fmt("vo-swirl",2); fmt("vo-diff",3); fmt("vo-count",0); const {ctx,w,h}=sizeCanvas(cv); ctx.fillStyle=`rgba(0,0,0,${0.045+val("vo-diff")})`; ctx.fillRect(0,0,w,h); ctx.fillStyle=ink(0.42); t+=0.01; for(const p of pts){ const old=[p[0],p[1]], f=flow(p[0],p[1]); p[0]=(p[0]+f[0]*0.0025+1)%1; p[1]=(p[1]+f[1]*0.0025+1)%1; ctx.globalAlpha=0.5; ctx.fillRect(p[0]*w,p[1]*h,1.1,1.1); if(Math.hypot(p[0]-old[0],p[1]-old[1])>.5){ p[0]=Math.random(); p[1]=Math.random(); } } ctx.globalAlpha=1; }
  function loop(){ if(active&&run) step(); raf=requestAnimationFrame(loop); }
  $id("vo-count").addEventListener("input",reset); ["vo-swirl","vo-diff"].forEach(id=>$id(id).addEventListener("input",()=>fmt(id,id==="vo-diff"?3:2)));
  $id("vo-pause").onclick=()=>{ run=!run; $id("vo-pause").textContent=run?"pause":"play"; };
  $id("vo-reset").onclick=reset; $id("vo-dl").onclick=()=>dlCanvas(cv,"serif_vorticity.png");
  window.addEventListener("resize",reset); reset(); visible(cv,v=>active=v); loop();
}

function makeThreeStage(containerId){
  const el=$id(containerId); if(!el) return null;
  const scene=new THREE.Scene(), camera=new THREE.PerspectiveCamera(42,1,0.1,1000), renderer=new THREE.WebGLRenderer({antialias:true,alpha:true,preserveDrawingBuffer:true});
  renderer.setClearColor(0x000000,1); el.appendChild(renderer.domElement); camera.position.set(0,0,5);
  const root=new THREE.Group(); scene.add(root);
  let rx=-0.35,ry=0.55,zoom=5,drag=false,lx=0,ly=0,active=false;
  function resize(){ const w=el.clientWidth||520,h=w; renderer.setSize(w,h,false); camera.aspect=w/h; camera.position.z=zoom; camera.updateProjectionMatrix(); }
  el.addEventListener("pointerdown",e=>{drag=true;lx=e.clientX;ly=e.clientY;el.setPointerCapture?.(e.pointerId);});
  el.addEventListener("pointermove",e=>{ if(!drag) return; ry+=(e.clientX-lx)*0.008; rx+=(e.clientY-ly)*0.008; lx=e.clientX;ly=e.clientY; });
  window.addEventListener("pointerup",()=>drag=false);
  el.addEventListener("wheel",e=>{ e.preventDefault(); zoom=Math.max(2,Math.min(12,zoom+Math.sign(e.deltaY)*0.35)); camera.position.z=zoom; },{passive:false});
  window.addEventListener("resize",resize); resize(); visible(el,v=>active=v);
  return {el,scene,camera,renderer,root,get active(){return active;},nudge(dx=0,dy=0){ ry+=dx; rx+=dy; },render(){ root.rotation.x=rx; root.rotation.y=ry; renderer.render(scene,camera); },resize};
}
function lineObj(points, color=0xf2efe8, opacity=.82){
  const geo=new THREE.BufferGeometry().setFromPoints(points.map(p=>new THREE.Vector3(p[0],p[1],p[2])));
  return new THREE.Line(geo,new THREE.LineBasicMaterial({color,transparent:true,opacity}));
}
function pointsObj(points, size=.025){
  const geo=new THREE.BufferGeometry().setFromPoints(points.map(p=>new THREE.Vector3(p[0],p[1],p[2])));
  return new THREE.Points(geo,new THREE.PointsMaterial({color:0xf2efe8,size,transparent:true,opacity:.85}));
}
function clear3(s){ while(s.root.children.length) s.root.remove(s.root.children[0]); }

function attractor3(container, kind){
  const s=makeThreeStage(container); if(!s) return {project:()=>[],setPlay:()=>{}}; let pts=[], playing=false, marker=null;
  function integrate(){
    clear3(s); pts=[]; marker=null; let x=.1,y=.1,z=.1, dt=.008, N=kind==="lor"?val("lor-trail")|0:kind==="ros"?val("ros-trail")|0:val("tho-trail")|0;
    for(let i=0;i<N;i++){
      let dx,dy,dz;
      if(kind==="lor"){ const sig=val("lor-s"),rho=val("lor-r"),beta=val("lor-b"); dx=sig*(y-x); dy=x*(rho-z)-y; dz=x*y-beta*z; dt=.006; }
      else if(kind==="ros"){ const a=val("ros-a"),b=val("ros-b"),c=val("ros-c"); dx=-(y+z); dy=x+a*y; dz=b+z*(x-c); dt=.018; }
      else { const b=val("tho-b"); dx=Math.sin(y)-b*x; dy=Math.sin(z)-b*y; dz=Math.sin(x)-b*z; dt=.045; }
      x+=dx*dt; y+=dy*dt; z+=dz*dt; if(i>80) pts.push([x,y,z]);
    }
    let max=0; for(const p of pts) max=Math.max(max,Math.abs(p[0]),Math.abs(p[1]),Math.abs(p[2])); const sc=1.65/(max||1);
    pts=pts.map(p=>[p[0]*sc,p[1]*sc,p[2]*sc]); s.root.add(lineObj(pts));
    marker=new THREE.Mesh(new THREE.SphereGeometry(.055,16,12),new THREE.MeshBasicMaterial({color:0xf2efe8}));
    s.root.add(marker);
    s.render();
  }
  function loop(now){ if(s.active||playing){ if(playing) s.nudge(.006,.0015); if(marker&&pts.length){ const p=pts[((now*.06)|0)%pts.length]; marker.position.set(p[0],p[1],p[2]); } s.render(); } requestAnimationFrame(loop); }
  integrate(); loop(0); return {reset:integrate,setPlay:v=>{playing=v;},project:()=>pts.map(p=>[p[0],p[1]])};
}

function phyllo3(){
  const s=makeThreeStage("phy-3d"); if(!s) return; function draw(){ clear3(s); fmt("ph-ang",2); fmt("ph-count",0); fmt("ph-shell",2); const N=val("ph-count")|0, ang=val("ph-ang")*Math.PI/180, shell=val("ph-shell"), pts=[]; for(let i=0;i<N;i++){ const r=Math.sqrt(i/N)*1.8, th=i*ang, x=r*Math.cos(th), y=r*Math.sin(th), z=0; const phi=Math.acos(1-2*(i+.5)/N), sph=[Math.sin(phi)*Math.cos(th)*1.65,Math.sin(phi)*Math.sin(th)*1.65,Math.cos(phi)*1.65]; pts.push([x*(1-shell)+sph[0]*shell,y*(1-shell)+sph[1]*shell,z*(1-shell)+sph[2]*shell]); } s.root.add(pointsObj(pts,.026)); }
  bindInputs(["ph-ang","ph-count","ph-shell"],draw); $id("ph-golden").onclick=()=>{$id("ph-ang").value=137.507; draw();}; $id("ph-brush").onclick=()=>{ const N=700,ang=val("ph-ang")*Math.PI/180,pts=[]; for(let i=0;i<N;i++){ const r=Math.sqrt(i); pts.push([r*Math.cos(i*ang),r*Math.sin(i*ang)]); } sendBrush("custom phyllotaxis",pts); }; function loop(){ if(s.active){ s.root.rotation.y+=0.002; s.render(); } requestAnimationFrame(loop); } draw(); loop();
}
function chladni3(){
  const s=makeThreeStage("ch-3d"); if(!s) return; function draw(){ clear3(s); ["ch-n","ch-m"].forEach(id=>fmt(id,0)); fmt("ch-height",2); const n=val("ch-n"),m=val("ch-m"),H=val("ch-height"), seg=70, verts=[], idx=[]; for(let y=0;y<=seg;y++)for(let x=0;x<=seg;x++){ const u=x/seg,v=y/seg,xx=(u-.5)*3,yy=(v-.5)*3,z=(Math.cos(n*Math.PI*u)*Math.cos(m*Math.PI*v)-Math.cos(m*Math.PI*u)*Math.cos(n*Math.PI*v))*H; verts.push(xx,yy,z); } for(let y=0;y<seg;y++)for(let x=0;x<seg;x++){ const a=y*(seg+1)+x; idx.push(a,a+1,a+seg+1,a+1,a+seg+2,a+seg+1); } const geo=new THREE.BufferGeometry(); geo.setAttribute("position",new THREE.Float32BufferAttribute(verts,3)); geo.setIndex(idx); geo.computeVertexNormals(); const mat=new THREE.MeshBasicMaterial({color:0xf2efe8,wireframe:true,transparent:true,opacity:.36}); s.root.add(new THREE.Mesh(geo,mat)); }
  bindInputs(["ch-n","ch-m","ch-height"],draw); let chLast=0; motionButton("ch-play","stop modes",t=>{ if(t-chLast<0.18) return; chLast=t; setCtl("ch-n",2+((t*1.8)|0)%8,0); setCtl("ch-m",3+((t*1.25+2)|0)%8,0); setCtl("ch-height",.45+.55*(.5+.5*Math.sin(t*1.1)),2); draw(); s.nudge(.012,.003); s.render(); }); $id("ch-swap").onclick=()=>{ const n=$id("ch-n").value; $id("ch-n").value=$id("ch-m").value; $id("ch-m").value=n; draw();}; $id("ch-rand").onclick=()=>{ $id("ch-n").value=1+(Math.random()*10|0); $id("ch-m").value=1+(Math.random()*10|0); draw();}; function loop(){ if(s.active) s.render(); requestAnimationFrame(loop); } draw(); loop();
}
function torus3(){
  const s=makeThreeStage("tor-3d"); if(!s) return; function draw(){ clear3(s); fmt("tor-tube",2); fmt("tor-twist",0); fmt("tor-auto",0); const tube=val("tor-tube"),tw=val("tor-twist"); const geo=new THREE.TorusGeometry(1.25,tube,24,130); const mesh=new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color:0xf2efe8,wireframe:true,transparent:true,opacity:.42})); s.root.add(mesh); const pts=[]; for(let i=0;i<900;i++){ const u=TAU*i/899*2,v=tw*u; pts.push([(1.25+tube*Math.cos(v))*Math.cos(u),(1.25+tube*Math.cos(v))*Math.sin(u),tube*Math.sin(v)]); } s.root.add(lineObj(pts,0xf2efe8,.95)); }
  bindInputs(["tor-tube","tor-twist","tor-auto"],draw); let torLast=0; motionButton("tor-play","stop twist",t=>{ if(t-torLast<0.08) return; torLast=t; setCtl("tor-twist",4+4*Math.sin(t*.9),0); setCtl("tor-tube",.34+.16*Math.sin(t*.6+1),2); draw(); s.nudge(.018,.002); s.render(); }); function loop(){ if(s.active){ if(val("tor-auto")) s.root.rotation.y+=0.004; s.render(); } requestAnimationFrame(loop); } draw(); loop();
}
function wave3(){
  const s=makeThreeStage("wav-3d"); if(!s) return; let sources=[[-.8,0,0],[.8,0,1.8]], time=0; function build(){ clear3(s); const seg=64, verts=[], idx=[]; const k=TAU/val("wav-len"), ph=val("wav-phase"), H=val("wav-height"); for(let y=0;y<=seg;y++)for(let x=0;x<=seg;x++){ const xx=(x/seg-.5)*3.2, yy=(y/seg-.5)*3.2; let z=0; sources.forEach((p,i)=>{ const r=Math.hypot(xx-p[0],yy-p[1]); z+=Math.sin(k*r-time+(i?ph:0))/(1+1.2*r); }); verts.push(xx,yy,z*H*.22); } for(let y=0;y<seg;y++)for(let x=0;x<seg;x++){ const a=y*(seg+1)+x; idx.push(a,a+1,a+seg+1,a+1,a+seg+2,a+seg+1); } const geo=new THREE.BufferGeometry(); geo.setAttribute("position",new THREE.Float32BufferAttribute(verts,3)); geo.setIndex(idx); s.root.add(new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color:0xf2efe8,wireframe:true,transparent:true,opacity:.36}))); s.root.add(pointsObj(sources.map(p=>[p[0],p[1],.18]),.08)); }
  bindInputs(["wav-len","wav-phase","wav-height"],()=>{["wav-len","wav-phase","wav-height"].forEach(id=>fmt(id,2)); build();}); motionButton("wav-play","stop waves",(t,dt)=>{ time+=dt*6; sources[0][1]=.32*Math.sin(t*.8); sources[1][1]=.32*Math.sin(t*.8+Math.PI); build(); s.render(); }); $id("wav-reset").onclick=()=>{ sources=[[-.8,0,0],[.8,0,1.8]]; time=0; build();}; function loop(){ if(s.active) s.render(); requestAnimationFrame(loop); } build(); loop();
}

function equationLabs(){
  elasticaLab(); deJongLab(); lissLab(); hypoLab(); rdLab(); fieldLab(); vortexLab();
  phyllo3(); chladni3(); torus3(); wave3();
  const lor=attractor3("lor-3d","lor"), ros=attractor3("ros-3d","ros"), tho=attractor3("tho-3d","tho");
  ["lor-s","lor-r","lor-b","lor-trail"].forEach(id=>$id(id).addEventListener("input",()=>{fmt(id,id==="lor-b"?2:id==="lor-trail"?0:1); lor.reset();}));
  ["ros-a","ros-b","ros-c","ros-trail"].forEach(id=>$id(id).addEventListener("input",()=>{fmt(id,id==="ros-c"?1:id==="ros-trail"?0:2); ros.reset();}));
  ["tho-b","tho-trail"].forEach(id=>$id(id).addEventListener("input",()=>{fmt(id,id==="tho-b"?3:0); tho.reset();}));
  let lorLast=0; motionButton("lor-play","stop weather",t=>{ if(t-lorLast<0.42) return; lorLast=t; setCtl("lor-r",29+10*Math.sin(t*.32),1); setCtl("lor-s",10+2.8*Math.sin(t*.21+1),1); lor.reset(); },v=>lor.setPlay(v));
  let rosLast=0; motionButton("ros-play","stop fold",t=>{ if(t-rosLast<0.46) return; rosLast=t; setCtl("ros-c",5.8+2.5*Math.sin(t*.28),1); setCtl("ros-a",.22+.12*Math.sin(t*.19+2),2); ros.reset(); },v=>ros.setPlay(v));
  let thoLast=0; motionButton("tho-play","stop damping",t=>{ if(t-thoLast<0.42) return; thoLast=t; setCtl("tho-b",.205+.055*Math.sin(t*.38),3); tho.reset(); },v=>tho.setPlay(v));
  $id("lor-reset").onclick=()=>lor.reset(); $id("ros-reset").onclick=()=>ros.reset(); $id("tho-reset").onclick=()=>tho.reset();
  $id("lor-brush").onclick=()=>sendBrush("custom lorenz",lor.project());
  $id("ros-brush").onclick=()=>sendBrush("custom rossler",ros.project());
  $id("tho-brush").onclick=()=>sendBrush("custom thomas",tho.project());
  ["lor-s","lor-r"].forEach(id=>fmt(id,1)); fmt("lor-b",2); fmt("lor-trail",0); ["ros-a","ros-b"].forEach(id=>fmt(id,2)); fmt("ros-c",1); fmt("ros-trail",0); fmt("tho-b",3); fmt("tho-trail",0);
}
window.addEventListener("load",equationLabs);
</script>
'''


def main():
    html = SRC.read_text()

    html = html.replace(
        '.card .ceq::-webkit-scrollbar{height:4px;}.card .ceq::-webkit-scrollbar-thumb{background:var(--mut2);}\n',
        '.card .ceq::-webkit-scrollbar{height:4px;}.card .ceq::-webkit-scrollbar-thumb{background:var(--mut2);}\n' + LAB_CSS + '\n',
    )

    start = html.index('<!-- 05 -->')
    end = html.index('\n<footer>', start)
    html = html[:start] + LAB_HTML + html[end:]

    old = 'const sel=$("br-curve").value, raw=sel==="S"?curveS():sel==="harmonograph"?curveH():curveL();'
    new = 'const sel=$("br-curve").value, raw=(sel==="custom"&&window.serifBrushPath)?window.serifBrushPath:(sel==="S"?curveS():sel==="harmonograph"?curveH():curveL());'
    html = html.replace(old, new)

    html = html.replace('\n</body>\n</html>\n', '\n' + LAB_JS + '\n</body>\n</html>\n')

    OUT.write_text(html)
    print(OUT)


if __name__ == "__main__":
    main()
