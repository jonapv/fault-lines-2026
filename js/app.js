'use strict';
const mechanisms={energy:'An energy shock can raise inflation and squeeze real incomes; tighter financing may then expose fiscal and credit vulnerabilities. Policy buffers can interrupt the chain.',funding:'Sovereign risk premia can affect collateral and bank balance sheets. Tighter credit and non-bank redemptions can transmit stress to market prices; this is a conditional amplification mechanism.',feedback:'Repricing can reduce wealth and collateral values. Weaker activity can lower tax receipts and worsen credit quality, feeding stress back into sovereign funding and financial intermediation.'};
function selectPath(path){
 document.querySelectorAll('[data-path]').forEach(b=>{const active=b.dataset.path===path;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
 document.querySelectorAll('[data-node]').forEach(n=>n.classList.toggle('selected',n.dataset.node===path));
 document.getElementById('map-explanation').textContent=mechanisms[path];
}
document.querySelectorAll('[data-path]').forEach(b=>b.addEventListener('click',()=>selectPath(b.dataset.path)));
selectPath('energy');
