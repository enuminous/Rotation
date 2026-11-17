"use strict";
// Rotation Lab: deterministic analytical illustrations, not empirical cosmic data.
(() => {
  const $ = (id) => document.getElementById(id);
  const TWO_PI = Math.PI * 2;
  const MODES = {
    vector: {
      name: "Vector rotation",
      number: "01",
      equation: "v = (-ωy, ωx, 0),     ∇ × v = (0, 0, 2ω)",
      description: "A prescribed rigid-body velocity field. Angular speed and vorticity differ by a factor of two. The circle, arrows and circulation are local kinematics—not universal cosmic rotation.",
      source: "docs/WHAT_ROTATION_MEANS.md",
      controls: [
        {key:"omega", label:"Angular speed ω", min:-2.5,max:2.5,step:0.05,value:0.8,unit:" rad/s"},
        {key:"radius",label:"Circulation radius",min:0.35,max:2.1,step:0.05,value:1.3,unit:""}
      ]
    },
    complex: {
      name: "Complex scalar",
      number: "02",
      equation: "ψ(r, φ, t) = f(r) exp[i(nφ + Ωt)]",
      description: "Hue encodes a complex U(1) scalar phase with integer winding n around a nodal core. A uniform time-phase rotation is not spatial vorticity; a physical superfluid requires an actual equation, current and units.",
      source: "docs/SCALAR_FIELDS.md",
      controls: [
        {key:"winding",label:"Winding number n",min:-4,max:4,step:1,value:2,unit:""},
        {key:"phaseRate",label:"Time-phase rate Ω",min:-3,max:3,step:0.05,value:0.6,unit:" rad/s"},
        {key:"core",label:"Nodal-core scale",min:0.08,max:0.7,step:0.02,value:0.22,unit:""}
      ]
    },
    real: {
      name: "Real scalar null",
      number: "03",
      equation: "φ(x, y) = αx² + βy² + c,      ∇ × ∇φ = 0",
      description: "This deliberately nonrotating counterexample matters. A smooth single-valued real scalar has a gradient, but the curl of that gradient is zero. Rotationally shaped level sets are not a nonzero intrinsic vorticity.",
      source: "docs/SCALAR_FIELDS.md",
      controls: [
        {key:"alpha",label:"X curvature α",min:-2,max:2,step:0.1,value:1.2,unit:""},
        {key:"beta",label:"Y curvature β",min:-2,max:2,step:0.1,value:0.6,unit:""},
        {key:"offset",label:"Scalar offset c",min:-2,max:2,step:0.1,value:-0.5,unit:""}
      ]
    },
    clifford: {
      name: "Clifford rotor",
      number: "04",
      equation: "R(θ) = cos(θ/2) − B sin(θ/2),     v′ = R v R̃",
      description: "The upper dial represents the spatial-vector SO(3) action; the lower dial shows the half-angle rotor in Spin(3). A 2π turn changes the rotor sign but leaves the vector rotation unchanged. This is standard geometry—not a universal physical angular velocity.",
      source: "docs/CLIFFORDS.md",
      controls: [
        {key:"theta0",label:"Initial angle θ₀",min:0,max:12.56637,step:0.05,value:0,unit:" rad"},
        {key:"rate",label:"Angle rate",min:-2,max:2,step:0.05,value:0.8,unit:" rad/s"}
      ]
    },
    fluid: {
      name: "Vorticity & strain",
      number: "05",
      equation: "u = (sx − ωy, ωx − sy),   div u = 0,   curl u = 2ω",
      description: "Lagrangian tracers evolve under an explicitly specified planar linear flow. Antisymmetric rotation is independent of symmetric, trace-free strain. Numerical stepping illustrates the model; this is not Navier–Stokes evolution or a proof of regularity.",
      source: "docs/BSAR_BRIDGE.md",
      controls: [
        {key:"omega",label:"Local angular speed ω",min:-2,max:2,step:0.05,value:0.9,unit:""},
        {key:"strain",label:"Strain magnitude s",min:-1.5,max:1.5,step:0.05,value:0.25,unit:""},
        {key:"count",label:"Tracer particles",min:20,max:120,step:10,value:70,unit:""}
      ]
    },
    cosmic: {
      name: "Cosmology & nulls",
      number: "06",
      equation: "H²(a) = A + (ω² − k)/a²,    k_eff = k − ω²",
      description: "ME-056 is a proposed scalar relation, not a derived rotating Einstein metric. Two distinct (k, ω) pairs with equal k−ω² trace the exact same expansion curve. This visualizes nonidentifiability; it is not a fit to the observed universe.",
      source: "docs/COSMOLOGY.md",
      controls: [
        {key:"omega",label:"Model rotation ω",min:-2,max:2,step:0.05,value:0.75,unit:""},
        {key:"k",label:"Curvature parameter k",min:-2,max:2,step:0.05,value:0.8,unit:""},
        {key:"a",label:"Selected scale factor a",min:0.5,max:4,step:0.05,value:1.6,unit:""},
        {key:"base",label:"Other expansion terms A",min:0.1,max:4,step:0.05,value:1.3,unit:""}
      ]
    }
  };
  const order = Object.keys(MODES);
  const p = {};
  for (const name of order) {
    p[name] = {};
    for (const control of MODES[name].controls) p[name][control.key] = control.value;
  }
  const state = {
    mode: "vector", p, t: 0, playing: true, speed: 1,
    particles: [], previousFrame: null, evidence: [], sources: new Map()
  };
  const canvas = $("lab-canvas");
  const ctx = canvas.getContext("2d");
  const W = canvas.width, H = canvas.height, C = [W/2, H/2], S = 124;
  const colors = { gold:"#e8bc73", aqua:"#79e1ce", vio:"#b79cfa", muted:"#92a9be", line:"#2d455d", light:"#e8f2fb" };
  const world = (x,y) => [C[0]+x*S,C[1]-y*S];
  const fmt = (value,digits=3) => {
    if (!Number.isFinite(value)) return "undefined";
    if (Math.abs(value)<1e-10) return "0";
    return Number(value.toFixed(digits)).toString();
  };
  function point(x,y,r,color) {
    ctx.beginPath();ctx.arc(x,y,r,0,TWO_PI);ctx.fillStyle=color;ctx.fill();
  }
  function line(a,b,color,width=1.2,dash=[]) {
    ctx.save();ctx.beginPath();ctx.setLineDash(dash);ctx.moveTo(a[0],a[1]);ctx.lineTo(b[0],b[1]);
    ctx.lineWidth=width;ctx.strokeStyle=color;ctx.stroke();ctx.restore();
  }
  function circle(x,y,r,color,width=1,dash=[]) {
    ctx.save();ctx.beginPath();ctx.setLineDash(dash);ctx.arc(x,y,r,0,TWO_PI);
    ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke();ctx.restore();
  }
  function arrow(a,b,color,width=2,head=8) {
    const dx=b[0]-a[0],dy=b[1]-a[1],angle=Math.atan2(dy,dx);
    if(Math.hypot(dx,dy)<0.1)return;
    line(a,b,color,width);
    line(b,[b[0]-head*Math.cos(angle-.46),b[1]-head*Math.sin(angle-.46)],color,width);
    line(b,[b[0]-head*Math.cos(angle+.46),b[1]-head*Math.sin(angle+.46)],color,width);
  }
  function text(s,x,y,color=colors.light,size=15,align="left",weight="500") {
    ctx.save();ctx.font=weight+" "+size+"px ui-sans-serif,system-ui,Segoe UI,Arial";
    ctx.fillStyle=color;ctx.textAlign=align;ctx.fillText(s,x,y);ctx.restore();
  }
  function backdrop(title,sub="") {
    ctx.clearRect(0,0,W,H);ctx.fillStyle="#091323";ctx.fillRect(0,0,W,H);
    const g=ctx.createRadialGradient(C[0],C[1],10,C[0],C[1],520);
    g.addColorStop(0,"#162b40");g.addColorStop(1,"#080f1e");
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    ctx.strokeStyle="#1d3247";ctx.lineWidth=1;
    for(let x=40;x<W;x+=62){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}
    for(let y=40;y<H;y+=62){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
    line([55,C[1]],[W-55,C[1]],"#38536d",1.6);
    line([C[0],H-42],[C[0],46],"#38536d",1.6);
    text(title,25,38,colors.light,17,"left","700");
    if(sub)text(sub,25,63,colors.muted,12);
    text("+x",W-58,C[1]-14,colors.muted,12);
    text("+y",C[0]+10,57,colors.muted,12);
  }
  function drawVector() {
    const q=p.vector,w=q.omega,r=q.radius,theta=w*state.t;
    backdrop("RIGID ROTATION / SO(3)","u = (-ωy, ωx), z = 0");
    for(const rr of [0.5,1.0,1.5,2.0])circle(C[0],C[1],rr*S,"#39536a",1.15,[4,6]);
    const R=r*S, a=[C[0],C[1]], b=[C[0]+R*Math.cos(theta),C[1]-R*Math.sin(theta)];
    circle(C[0],C[1],R,"#a98b59",2);
    arrow(a,b,colors.gold,4,16);point(...b,9,"#fae2a9");
    const tipVel=[-w*r*Math.sin(theta),w*r*Math.cos(theta)];
    arrow(b,[b[0]+tipVel[0]*S*.44,b[1]-tipVel[1]*S*.44],colors.aqua,3.1,12);
    for(let x=-2;x<=2;x+=.8)for(let y=-1.6;y<=1.6;y+=.8) {
      const m=Math.hypot(x,y), vx=-w*y,vy=w*x,len=Math.hypot(vx,vy);
      if(m<.28||len<1e-8)continue;
      const norm=.23/Math.max(.8,len),a0=world(x,y),a1=world(x+vx*norm,y+vy*norm);
      arrow(a0,a1,"#577c8e",1.5,5);
    }
    text("ω = "+fmt(w)+" rad/s",20,H-49,colors.gold,17);
    text("curl u = "+fmt(2*w)+" z-hat",20,H-22,colors.aqua,14);
    text("Moving point",b[0]+15,b[1]-15,colors.gold,12);
  }
  function drawComplex() {
    const q=p.complex,n=q.winding,phase=q.phaseRate*state.t,core=q.core;
    backdrop("COMPLEX SCALAR / U(1)","Hue = phase arg(ψ), brightness = |ψ|");
    const dx=17,dy=17;
    for(let py=77;py<H-42;py+=dy){
      for(let px=50;px<W-50;px+=dx){
        const x=(px-C[0])/S,y=(C[1]-py)/S,r=Math.hypot(x,y);
        const amp=n===0?1:Math.tanh(r/core);
        const theta=n*Math.atan2(y,x)+phase;
        const hue=((theta*180/Math.PI)%360+360)%360;
        ctx.fillStyle="hsl("+hue+" 75% "+(17+amp*40)+"%)";
        ctx.fillRect(px,py,dx+1,dy+1);
      }
    }
    for(const rr of [.52,1.05,1.8])circle(C[0],C[1],rr*S,"#e7edf8a0",1.5,[7,7]);
    if(n!==0){
      point(C[0],C[1],Math.max(2,core*S*.45),"#090e17");
      for(let j=0;j<12;j++){
        const a=TWO_PI*j/12, c=world(1.4*Math.cos(a),1.4*Math.sin(a));
        arrow(c,world(1.4*Math.cos(a+.10*Math.sign(n)),1.4*Math.sin(a+.10*Math.sign(n))),"#f6eddb",2,6);
      }
    }
    text("Loop winding n = "+n,25,H-24,colors.light,18);
    text("ψ = f(r) exp[i(nφ+Ωt)]",W-25,H-24,"#f3e1a8",15,"right");
  }
  function drawReal() {
    const q=p.real;
    backdrop("REAL SCALAR / CURL-FREE CONTROL","φ(x,y) = αx² + βy² + c; curl(grad φ) = 0");
    const dx=20,dy=20;
    for(let py=78;py<H-40;py+=dy){
      for(let px=50;px<W-50;px+=dx){
        const x=(px-C[0])/S,y=(C[1]-py)/S;
        const phi=q.alpha*x*x+q.beta*y*y+q.offset;
        const z=Math.tanh(phi/3),hue=z>0?203:29;
        const light=20+Math.abs(z)*34;
        ctx.fillStyle="hsl("+hue+" 51% "+light+"%)";
        ctx.fillRect(px,py,dx+1,dy+1);
      }
    }
    for(let x=-2.5;x<=2.5;x+=.65)for(let y=-1.8;y<=1.8;y+=.62){
      const dx=2*q.alpha*x,dy=2*q.beta*y;
      const len=Math.hypot(dx,dy);
      if(len<.05)continue;
      const a=world(x,y),k=.23/Math.max(len,1),b=world(x+dx*k,y+dy*k);
      arrow(a,b,"#edce9c",1.6,6);
    }
    text("Gradient arrows ≠ rotational flow",25,H-22,colors.gold,16);
  }
  function drawClifford(){
    const q=p.clifford,theta=q.theta0+q.rate*state.t;
    backdrop("CLIFFORD / SPINOR DOUBLE COVER","Vector angle θ; rotor angle θ/2");
    const centers=[[245,325],[711,325]],r=143;
    for(const c of centers)circle(c[0],c[1],r,"#62788d",2);
    const v=centers[0],spin=centers[1];
    arrow(v,[v[0]+r*Math.cos(theta),v[1]-r*Math.sin(theta)],colors.aqua,4.5,14);
    arrow(spin,[spin[0]+r*Math.cos(theta/2),spin[1]+r*Math.sin(theta/2)],colors.gold,4.5,14);
    text("SO(3) VECTOR",v[0],122,colors.aqua,18,"center","700");
    text("Spin(3) ROTOR",spin[0],122,colors.gold,18,"center","700");
    text("θ",v[0],505,colors.light,19,"center");
    text("θ/2",spin[0],505,colors.light,19,"center");
    text("R = "+fmt(Math.cos(theta/2),4)+" − B("+fmt(Math.sin(theta/2),4)+")",W/2,H-34,"#e6d3b0",17,"center");
  }
  function velocity(x,y,w,s){return [s*x-w*y,w*x-s*y];}
  function seed(i,count){
    const t=i*2.399963229728653;
    const rr=.35+1.72*Math.sqrt((i+.5)/count);
    return {x:rr*Math.cos(t),y:rr*Math.sin(t),trail:[],i:i};
  }
  function resetParticles(){state.particles=Array.from({length:p.fluid.count},(_,i)=>seed(i,p.fluid.count));}
  function advect(dt){
    const q=p.fluid,w=q.omega,s=q.strain;
    // RK4 for analytic prescribed vector field only; not a Navier-Stokes solver.
    for(const particle of state.particles){
      let x=particle.x,y=particle.y;
      const a=velocity(x,y,w,s),b=velocity(x+dt*a[0]/2,y+dt*a[1]/2,w,s);
      const c=velocity(x+dt*b[0]/2,y+dt*b[1]/2,w,s),d=velocity(x+dt*c[0],y+dt*c[1],w,s);
      particle.x=x+dt*(a[0]+2*b[0]+2*c[0]+d[0])/6;
      particle.y=y+dt*(a[1]+2*b[1]+2*c[1]+d[1])/6;
      particle.trail.push([particle.x,particle.y]);
      if(particle.trail.length>20)particle.trail.shift();
      if(!Number.isFinite(particle.x)||Math.max(Math.abs(particle.x),Math.abs(particle.y))>3.25){
        const re=seed(particle.i,p.fluid.count);
        particle.x=re.x;particle.y=re.y;particle.trail=[];
      }
    }
  }
  function drawFluid(){
    const q=p.fluid,w=q.omega,s=q.strain;
    backdrop("VORTICITY / STRAIN / TRACERS","u = (sx−ωy, ωx−sy), divergence = 0");
    for(let x=-2.8;x<=2.8;x+=.58)for(let y=-2.1;y<=2.1;y+=.58){
      const v=velocity(x,y,w,s),len=Math.hypot(...v);
      if(len<.05)continue;
      const scale=.25/Math.max(1,len),a=world(x,y);
      arrow(a,world(x+v[0]*scale,y+v[1]*scale),"#496e81",1.3,5);
    }
    for(const t of state.particles){
      const color=t.i%4===0?colors.gold:colors.aqua;
      for(let i=1;i<t.trail.length;i++)
        line(world(...t.trail[i-1]),world(...t.trail[i]),color,.5+2.0*i/t.trail.length);
      const pos=world(t.x,t.y);point(...pos,2.5,color);
    }
    text("antisymmetric rotation: ω = "+fmt(w),25,H-46,colors.gold,14);
    text("symmetric strain: s = "+fmt(s)+"; curl = "+fmt(2*w),25,H-23,colors.aqua,14);
  }
  function cosmicValue(q,a){return q.base+(q.omega*q.omega-q.k)/(a*a);}
  function drawCosmic(){
    const q=p.cosmic;
    ctx.clearRect(0,0,W,H);ctx.fillStyle="#0a1423";ctx.fillRect(0,0,W,H);
    const left=85,right=W-45,top=96,bottom=H-79,amin=.5,amax=4;
    const degW=Math.sqrt(q.omega*q.omega+1),degK=q.k+1;
    const values=[];
    for(let i=0;i<=260;i++){let a=amin+(amax-amin)*i/260;values.push(cosmicValue(q,a),q.base-q.k/(a*a));}
    let ymin=Math.min(0,...values),ymax=Math.max(0,...values);
    if(Math.abs(ymax-ymin)<1e-5){ymin-=1;ymax+=1}
    let pad=Math.max(.2,(ymax-ymin)*.11);ymin-=pad;ymax+=pad;
    const mapX=a=>left+(a-amin)/(amax-amin)*(right-left),mapY=h=>bottom-(h-ymin)/(ymax-ymin)*(bottom-top);
    ctx.strokeStyle="#2b3b50";ctx.lineWidth=1;
    for(let i=0;i<=8;i++){let x=left+i/8*(right-left);line([x,top],[x,bottom],"#27394c",1);let a=amin+i/8*(amax-amin);text(fmt(a,1),x,bottom+23,colors.muted,12,"center");}
    for(let i=0;i<=6;i++){let val=ymin+i/6*(ymax-ymin);let y=mapY(val);line([left,y],[right,y],"#27394c",1);text(fmt(val,2),left-9,y+4,colors.muted,12,"right");}
    if(ymin<0&&ymax>0)line([left,mapY(0)],[right,mapY(0)],"#a96c67",1.3,[5,4]);
    text("ME-056 SCALAR EQUATION / MODEL NONIDENTIFIABILITY",25,36,colors.light,17,"left","700");
    text("x = scale factor a; y = H² (toy units). Not an Einstein solution or observed fit.",25,58,colors.muted,12);
    const trace=(fn,color,width,dash=[])=>{
      ctx.save();ctx.beginPath();ctx.setLineDash(dash);let started=false;
      for(let i=0;i<=300;i++){let a=amin+(amax-amin)*i/300,y=mapY(fn(a));if(!Number.isFinite(y))continue;if(!started){ctx.moveTo(mapX(a),y);started=true}else ctx.lineTo(mapX(a),y)}
      ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke();ctx.restore();
    };
    trace(a=>q.base-q.k/(a*a),"#a09fb8",2,[6,8]);
    trace(a=>q.base+(degW*degW-degK)/(a*a),colors.gold,6);
    trace(a=>cosmicValue(q,a),colors.aqua,2.5,[9,3]);
    const h=cosmicValue(q,q.a),xx=mapX(q.a),yy=mapY(h);
    line([xx,top],[xx,bottom],"#d6e1ea",1,[4,6]);point(xx,yy,8,colors.aqua);
    text("Selected H² = "+fmt(h),xx+14,yy-12,colors.aqua,13);
    text("teal: (k, ω)       gold: (k+1, sqrt(ω²+1))       gray: ω=0 with fixed k",
         W/2,H-31,colors.light,12,"center");
    text("Two distinct parameter sets give exactly the same teal/gold curve.",W/2,H-11,colors.gold,12,"center");
  }
  function computeMetrics(){
    const mode=state.mode,q=p[mode],t=state.t;
    if(mode==="vector"){
      const theta=q.omega*t;
      return [["Angular speed ω",fmt(q.omega)+" rad/s"],
      ["Vorticity ∇×u",fmt(2*q.omega)+" ẑ /s"],
      ["Circulation Γ",fmt(2*Math.PI*q.omega*q.radius*q.radius)],
      ["Curl flux",fmt(2*q.omega*Math.PI*q.radius*q.radius)],
      ["Particle angle",fmt(theta)+" rad"],
      ["Divergence","0"]];
    }
    if(mode==="complex")return [
      ["Winding number n",String(q.winding)],["Time phase Ωt",fmt(q.phaseRate*t)+" rad"],
      ["Phase around loop",fmt(TWO_PI*q.winding)+" rad"],["Nodal core",q.winding?"present":"not required"],
      ["Gauge status","model-dependent"],["Cosmic inference","none"]];
    if(mode==="real"){
      const phi=q.alpha+q.beta*.25+q.offset;
      return [["Scalar φ(1,0.5)",fmt(phi)],["∂xφ(1,0.5)",fmt(2*q.alpha)],
      ["∂yφ(1,0.5)",fmt(q.beta)],["Curl(∇φ)","0"],
      ["Input rank","real scalar"],["Universal vorticity","not implied"]];
    }
    if(mode==="clifford"){
      const theta=q.theta0+q.rate*t;
      return [["Vector angle",fmt(theta)+" rad"],["Rotor half-angle",fmt(theta/2)+" rad"],
        ["Scalar rotor part",fmt(Math.cos(theta/2),5)],["Bivector coefficient",fmt(-Math.sin(theta/2),5)],
        ["Rotor norm²","1"],["Sign at +2π","reversed"]];
    }
    if(mode==="fluid"){
      const v=velocity(1,.5,q.omega,q.strain),rank=Math.abs(q.omega)>Math.abs(q.strain)?"rotation-dominant":Math.abs(q.omega)<Math.abs(q.strain)?"strain-dominant":"boundary";
      return [["Vorticity ζ",fmt(2*q.omega)],["Divergence","0"],
       ["Symmetric strain",fmt(q.strain)],["Velocity u(1,0.5)",fmt(v[0])+", "+fmt(v[1])],
       ["Tracer count",String(state.particles.length)],["Flow regime",rank]];
    }
    const h=cosmicValue(q,q.a),altW=Math.sqrt(q.omega*q.omega+1),eff=q.k-q.omega*q.omega;
    return [["Effective curvature",fmt(eff)],["H²(a)",fmt(h)],
      ["Real H possible?",h<0?"NO at selected a":"YES; ± branches"],["Degenerate k′",fmt(q.k+1)],
      ["Degenerate ω′",fmt(altW)],["Curve difference","0 (by construction)"]];
  }
  function renderMetrics(){
    const target=$("metric-grid");target.replaceChildren();
    for(const [label,value] of computeMetrics()){
      const box=document.createElement("div");box.className="metric";
      const name=document.createElement("div");name.className="metric-label";name.textContent=label;
      const val=document.createElement("div");val.className="metric-value";val.textContent=value;
      box.append(name,val);target.append(box);
    }
  }
  function draw(){
    if(state.mode==="vector")drawVector();
    else if(state.mode==="complex")drawComplex();
    else if(state.mode==="real")drawReal();
    else if(state.mode==="clifford")drawClifford();
    else if(state.mode==="fluid")drawFluid();
    else drawCosmic();
    renderMetrics();
    $("time-value").textContent=fmt(state.t,2)+" s";
  }
  function renderControls(){
    const model=MODES[state.mode],q=p[state.mode],target=$("control-list");target.replaceChildren();
    for(const control of model.controls){
      const wrap=document.createElement("div");wrap.className="control-item";
      const label=document.createElement("label"),name=document.createElement("span"),value=document.createElement("output");
      const range=document.createElement("input");const bounds=document.createElement("div");
      const a=document.createElement("span"),b=document.createElement("span");
      const id="control-"+control.key;
      label.htmlFor=id;name.textContent=control.label;value.className="value";value.textContent=fmt(q[control.key],control.step===1?0:2)+control.unit;
      label.append(name,value);
      range.type="range";range.id=id;range.min=String(control.min);range.max=String(control.max);range.step=String(control.step);
      range.value=String(q[control.key]);range.setAttribute("aria-label",control.label);
      range.addEventListener("input",()=>{
        const next=Number(range.value);q[control.key]=next;
        value.textContent=fmt(next,control.step===1?0:2)+control.unit;
        if(state.mode==="fluid"&&control.key==="count")resetParticles();
        draw();
      });
      bounds.className="range-bound";a.textContent=fmt(control.min);b.textContent=fmt(control.max);
      bounds.append(a,b);wrap.append(label,range,bounds);target.append(wrap);
    }
    $("model-equation").textContent=model.equation;
    $("model-description").textContent=model.description;
    $("model-link").href=model.source;
    $("mode-heading").textContent=model.name;
    for(const button of document.querySelectorAll("[data-mode]"))
      button.setAttribute("aria-pressed",String(button.dataset.mode===state.mode));
  }
  function switchMode(mode,reset=true){
    if(!MODES[mode])return;
    state.mode=mode;
    if(reset)state.t=0;
    if(mode==="fluid")resetParticles();
    const url=new URL(window.location.href);url.searchParams.set("mode",mode);
    history.replaceState(null,"",url.toString());
    renderControls();draw();
  }
  function playButton(){
    $("play").textContent=state.playing?"Pause":"Play";
    $("play").setAttribute("aria-pressed",String(state.playing));
  }
  function togglePlay(){state.playing=!state.playing;playButton();}
  function reset(){
    state.t=0;
    if(state.mode==="fluid")resetParticles();
    draw();
  }
  function step(){
    state.playing=false;playButton();
    const dt=.1*state.speed;state.t+=dt;
    if(state.mode==="fluid")for(let i=0;i<3;i++)advect(dt/3);
    draw();
  }
  function advance(dt){
    state.t+=dt;
    if(state.mode==="fluid")for(let i=0;i<Math.max(1,Math.ceil(dt/.02));i++){
      const n=Math.max(1,Math.ceil(dt/.02));advect(dt/n);
    }
  }
  function tick(timestamp){
    if(state.previousFrame!==null && state.playing){
      const delta=Math.min(.05,Math.max(0,(timestamp-state.previousFrame)/1000))*state.speed;
      if(delta>0){advance(delta);draw();}
    }
    state.previousFrame=timestamp;
    requestAnimationFrame(tick);
  }
  function csvValue(value){
    const s=String(value);return /[",\r\n]/.test(s)?'"'+s.replace(/"/g,'""')+'"':s;
  }
  function exportCSV(){
    const mode=state.mode,q=p[mode],rows=[["model","x_or_a_or_theta","y_or_phase","value_1","value_2","interpretation"]];
    if(mode==="cosmic"){
      const altOmega=Math.sqrt(q.omega*q.omega+1),altK=q.k+1;
      for(let i=0;i<=150;i++){
        const a=.5+3.5*i/150;
        rows.push(["ME056",a,0,cosmicValue(q,a),q.base+(altOmega*altOmega-altK)/(a*a),"two degenerate H2 scalar curves"]);
      }
    }else if(mode==="clifford"){
      for(let i=0;i<=180;i++){const theta=4*Math.PI*i/180;
        rows.push(["Clifford",theta,theta/2,Math.cos(theta/2),-Math.sin(theta/2),"half-angle rotor coefficients"]);}
    }else if(mode==="vector"){
      for(let i=0;i<=180;i++){const theta=TWO_PI*i/180;
        rows.push(["rigid",q.radius*Math.cos(theta),q.radius*Math.sin(theta),-q.omega*q.radius*Math.sin(theta),q.omega*q.radius*Math.cos(theta),"x,y,u_x,u_y"]);}
    }else if(mode==="fluid"){
      for(let i=-15;i<=15;i++)for(let j=-15;j<=15;j++){
        const x=i/10,y=j/10,v=velocity(x,y,q.omega,q.strain);
        rows.push(["linear_flow",x,y,v[0],v[1],"x,y,u_x,u_y"]);}
    }else if(mode==="real"){
      for(let i=-20;i<=20;i++)for(let j=-20;j<=20;j++){
        const x=i/10,y=j/10;rows.push(["real_scalar",x,y,q.alpha*x*x+q.beta*y*y+q.offset,0,"phi(x,y); curl grad phi = 0"]);}
    }else{
      for(let i=0;i<=180;i++){const a=TWO_PI*i/180,phase=q.winding*a+q.phaseRate*state.t;
        rows.push(["complex_scalar",a,phase,Math.cos(phase),Math.sin(phase),"phase along nonzero loop; not cosmic observation"]);}
    }
    const csv=rows.map(row=>row.map(csvValue).join(",")).join("\r\n")+"\r\n";
    const blob=new Blob([csv],{type:"text/csv;charset=utf-8"}),url=URL.createObjectURL(blob),a=document.createElement("a");
    a.href=url;a.download="rotation-lab-"+mode+"-toy.csv";document.body.append(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1000);
    $("export-note").textContent="Toy data exported. These are analytic/model values, NOT measurements.";
  }
  function evidenceClass(status){
    if(status==="OBSERVED_LOCAL")return "local";
    if(status==="MODEL_CONSTRAINT")return "constraint";
    if(["OPEN","REPORTED_CONTESTED","PROPOSED_MODEL"].includes(status))return "open";
    return "";
  }
  function renderEvidence(){
    const query=$("search").value.trim().toLowerCase(),status=$("status-filter").value,domain=$("domain-filter").value;
    const found=state.evidence.filter(c=>(!status||c.status===status)&&(!domain||c.domain===domain)&&
      (!query||[c.claim,c.id,c.description,c.limits,c.domain,...c.source_ids].join(" ").toLowerCase().includes(query)));
    $("evidence-count").textContent=found.length+" of "+state.evidence.length+" evidence entries";
    const root=$("evidence-cards");root.replaceChildren();
    if(found.length===0){const e=document.createElement("div");e.className="empty";e.textContent="No matching claims. Try a broader query.";root.append(e);}
    for(const c of found){
      const card=document.createElement("article");card.className="evidence-card";
      const tag=document.createElement("span");tag.className="tag "+evidenceClass(c.status);tag.textContent=c.status.replaceAll("_"," ");
      const title=document.createElement("h3");title.textContent=c.claim;
      const id=document.createElement("div");id.className="evidence-id";id.textContent=c.id+" · "+c.domain;
      const desc=document.createElement("p");desc.textContent=c.description;
      const limit=document.createElement("p");limit.className="limits";limit.textContent="Boundary: "+c.limits;
      const sources=document.createElement("div");sources.className="sources";
      for(const srcId of c.source_ids){
        const src=state.sources.get(srcId);
        if(!src)continue;
        const link=document.createElement("a");link.href=src.url;link.rel="noopener noreferrer";
        link.target="_blank";link.textContent=srcId;link.title=src.title;sources.append(link);
      }
      card.append(tag,title,id,desc,limit,sources);root.append(card);
    }
  }
  async function loadEvidence(){
    try{
      const responses=await Promise.all([fetch("./data/evidence.json"),fetch("./data/sources.json")]);
      if(responses.some(r=>!r.ok))throw new Error("Evidence registry unavailable");
      const [ev,sr]=await Promise.all(responses.map(r=>r.json()));
      state.evidence=ev.evidence;state.sources=new Map(sr.sources.map(x=>[x.id,x]));
      for(const status of ev.status_vocabulary){
        const opt=document.createElement("option");opt.value=status;opt.textContent=status.replaceAll("_"," ");
        $("status-filter").append(opt);
      }
      for(const domain of [...new Set(ev.evidence.map(x=>x.domain))].sort()){
        const opt=document.createElement("option");opt.value=domain;opt.textContent=domain;
        $("domain-filter").append(opt);
      }
      $("evidence-stats").textContent=ev.evidence.length+" claims / "+sr.sources.length+" referenced sources";
      renderEvidence();
    }catch(error){
      $("evidence-count").textContent="Evidence JSON could not be loaded. Serve this repository with python -m http.server 8000 or enable GitHub Pages.";
      console.error(error);
    }
  }
  // Controls are bound once and perform the labeled actions.
  for(const button of document.querySelectorAll("[data-mode]")){
    button.addEventListener("click",()=>switchMode(button.dataset.mode));
  }
  $("play").addEventListener("click",togglePlay);
  $("reset").addEventListener("click",reset);
  $("step").addEventListener("click",step);
  $("export-csv").addEventListener("click",exportCSV);
  $("speed").addEventListener("change",()=>{state.speed=Number($("speed").value);});
  for(const id of ["search","status-filter","domain-filter"])
    $(id).addEventListener("input",renderEvidence);
  window.addEventListener("keydown",ev=>{
    if(["INPUT","SELECT","TEXTAREA"].includes(document.activeElement.tagName)||ev.altKey||ev.metaKey||ev.ctrlKey)return;
    if(ev.code==="Space"){ev.preventDefault();togglePlay();}
    else if(ev.key==="r"||ev.key==="R")reset();
    else if(/^[1-6]$/.test(ev.key))switchMode(order[Number(ev.key)-1]);
  });
  if(window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches)state.playing=false;
  const fromQuery=new URL(window.location.href).searchParams.get("mode");
  if(MODES[fromQuery])state.mode=fromQuery;
  resetParticles();
  playButton();
  renderControls();
  draw();
  loadEvidence();
  requestAnimationFrame(tick);
})();
