'use strict';
// Local SVG keeps this research note usable without a CDN, API or chart dependency.
for (const c of window.FAULT_LINES_SERIES) {
  const target=document.getElementById('chart-'+c.id);
  const W=520,H=260,pad={l:48,r:20,t:18,b:45};
  const lo=c.kind==='bar'?0:Math.floor(Math.min(...c.values)-Math.max((Math.max(...c.values)-Math.min(...c.values))*.2,.3));
  const hi=Math.ceil(Math.max(...c.values)+Math.max((Math.max(...c.values)-lo)*.12,.3));
  const x=i=>pad.l+(i+.5)*(W-pad.l-pad.r)/c.values.length;
  const y=v=>H-pad.b-(v-lo)/(hi-lo)*(H-pad.b-pad.t);
  const ns='http://www.w3.org/2000/svg';
  const svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox',`0 0 ${W} ${H}`);svg.setAttribute('role','group');svg.setAttribute('aria-label',c.title+'; values also available in the data table.');
  function add(name,attrs,text){const e=document.createElementNS(ns,name);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));if(text!==undefined)e.textContent=text;svg.append(e);return e;}
  for(let i=0;i<5;i++){const v=lo+(hi-lo)*i/4;add('line',{x1:pad.l,y1:y(v),x2:W-pad.r,y2:y(v),stroke:'#d7cfc2','stroke-width':.7});add('text',{x:pad.l-9,y:y(v)+4,'text-anchor':'end'},Number(v.toFixed(1)));}
  if(c.kind==='line')add('polyline',{points:c.values.map((v,i)=>`${x(i)},${y(v)}`).join(' '),fill:'none',stroke:'#642832','stroke-width':2});
  c.values.forEach((v,i)=>{
    const shape=c.kind==='bar'?add('rect',{x:x(i)-(W-pad.l-pad.r)/c.values.length*.27,y:y(v),width:(W-pad.l-pad.r)/c.values.length*.54,height:y(0)-y(v),fill:'#642832'}):add('circle',{cx:x(i),cy:y(v),r:4,fill:'#642832',stroke:'#f4f0e7','stroke-width':1.5});
    shape.setAttribute('class','point');shape.setAttribute('tabindex','0');shape.setAttribute('aria-label',`${c.labels[i]}: ${v} ${c.unit}`);
    const title=document.createElementNS(ns,'title');title.textContent=`${c.labels[i]}: ${v} ${c.unit}`;shape.append(title);
    const show=()=>document.getElementById('readout-'+c.id).textContent=`${c.labels[i]} · ${v} ${c.unit}`;
    shape.addEventListener('pointerenter',show);shape.addEventListener('focus',show);shape.addEventListener('click',show);
    if(c.labels.length<9||i%2===0||i===c.labels.length-1)add('text',{x:x(i),y:H-19,'text-anchor':'middle'},c.labels[i]);
  });target.append(svg);
}
