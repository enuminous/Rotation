"use strict";
// A dependency-free DOM/canvas simulation to detect JS startup and control errors.
// No browser security, canvas pixel, or physical science conclusions are asserted.
const fs=require("node:fs");
const vm=require("node:vm");
const assert=require("node:assert/strict");
const path=require("node:path");
const root=path.resolve(__dirname,"..");
const html=fs.readFileSync(path.join(root,"index.html"),"utf8");
const src=fs.readFileSync(path.join(root,"assets/rotation-lab.js"),"utf8");
const required=["lab-canvas","control-list","model-equation","model-description","model-link",
 "metric-grid","mode-heading","time-value","play","reset","step","export-csv",
 "export-note","speed","search","status-filter","domain-filter","evidence-stats",
 "evidence-count","evidence-cards"];
for(const id of required)assert(html.includes('id="'+id+'"'),"Missing DOM id: "+id);
assert(html.includes('src="./assets/rotation-lab.js"'),"Script is not loaded");
assert(html.includes('href="./assets/rotation-lab.css"'),"CSS is not loaded");
const modes=["vector","complex","real","clifford","fluid","cosmic"];
for(const mode of modes)assert(html.includes('data-mode="'+mode+'"'),"Missing mode control: "+mode);
class El{
  constructor(tag="div"){this.tagName=tag.toUpperCase();this.children=[];this.listeners={};
    this.attributes={};this.dataset={};this.value="";this.textContent="";this.style={};this.href="";this.id="";}
  append(...x){this.children.push(...x)}
  appendChild(x){this.children.push(x)}
  replaceChildren(...x){this.children=[...x]}
  remove(){}
  setAttribute(k,v){this.attributes[k]=v}
  addEventListener(k,fn){(this.listeners[k]??=[]).push(fn)}
  fire(k){for(const fn of this.listeners[k]||[])fn({type:k,preventDefault(){}})}
  click(){this.fire("click")}
}
let gradients=0;
const canvasCtx=new Proxy({}, {get:(obj,k)=>{
  if(k==="createRadialGradient")return ()=>({addColorStop(){gradients++}});
  return obj[k]??(()=>{});
},set:(obj,k,v)=>{obj[k]=v;return true}});
const elements=new Map(required.map(id=>[id,new El()]));
const canvas=elements.get("lab-canvas");canvas.width=960;canvas.height=640;canvas.getContext=()=>canvasCtx;
elements.get("speed").value="1";
const buttons=modes.map(mode=>{const b=new El("button");b.dataset.mode=mode;return b});
const body=new El("body");
const document={
  body,activeElement:{tagName:"BODY"},
  getElementById:(id)=>{assert(elements.has(id),"Unexpected DOM id: "+id);return elements.get(id)},
  createElement:(tag)=>new El(tag),
  querySelectorAll:(sel)=>{assert.equal(sel,"[data-mode]");return buttons}
};
const location={href:"http://localhost:8000/index.html"};
const history={replaceState(_a,_b,url){location.href=String(url)}};
class MockURL extends URL{
  static createObjectURL(_blob){MockURL.created=(MockURL.created||0)+1;return "blob:rotation-test"}
  static revokeObjectURL(_url){}
}
let pendingAnimation=null;
const window={location,history,matchMedia:()=>({matches:true}),
 addEventListener:(event,fn)=>{window.listeners[event]=fn},listeners:{}};
const sources=JSON.parse(fs.readFileSync(path.join(root,"data/sources.json"),"utf8"));
const evidence=JSON.parse(fs.readFileSync(path.join(root,"data/evidence.json"),"utf8"));
const fetch=(url)=>Promise.resolve({ok:true,json:async()=>url.includes("evidence.json")?evidence:sources});
const consoleStub={log(){},warn(){},error(...args){throw new Error("JS console.error: "+args.join(" "))}};
const scriptContext={window,document,history,URL:MockURL,Blob,fetch,
 requestAnimationFrame:(fn)=>{pendingAnimation=fn;return 1},
 setTimeout:()=>0, console:consoleStub};
vm.runInNewContext(src,scriptContext,{filename:"assets/rotation-lab.js",timeout:8000});
assert.equal(elements.get("mode-heading").textContent,"Vector rotation");
assert.equal(elements.get("metric-grid").children.length,6);
for(let i=0;i<modes.length;i++){
  buttons[i].fire("click");
  const heading=elements.get("mode-heading").textContent;
  assert(heading.length>3,"Mode heading missing "+modes[i]);
  assert.equal(elements.get("metric-grid").children.length,6,"Metrics missing "+modes[i]);
  assert(elements.get("control-list").children.length>=2,"Controls missing "+modes[i]);
  assert.equal(buttons[i].attributes["aria-pressed"],"true");
  const item=elements.get("control-list").children[0];
  const slider=item.children[1];
  assert(slider.listeners.input?.length===1,"Missing input callback "+modes[i]);
  slider.value=slider.max;
  slider.fire("input");
  elements.get("reset").fire("click");
  elements.get("step").fire("click");
  assert(elements.get("time-value").textContent.includes("s"));
  elements.get("export-csv").fire("click");
  assert(elements.get("export-note").textContent.includes("Toy data exported"));
}
assert.equal(MockURL.created,6,"CSV exports did not all fire");
assert(pendingAnimation,"Animation not scheduled");
(async()=>{
  await Promise.resolve();await Promise.resolve();await new Promise(setImmediate);
  assert.equal(elements.get("evidence-cards").children.length,26,"Evidence cards did not load");
  elements.get("status-filter").value="OPEN";
  elements.get("status-filter").fire("input");
  assert(elements.get("evidence-cards").children.length<26);
  elements.get("status-filter").value="";
  elements.get("status-filter").fire("input");
  assert.equal(elements.get("evidence-cards").children.length,26);
  console.log("PASS: six modes, sliders, metrics, resets, step, CSV, 26 evidence cards and filters");
})().catch(e=>{console.error(e);process.exitCode=1});
