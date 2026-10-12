/* CCE v20261012-3: reveal, counters, library filter, sort, stepper, flip */
(function(){"use strict";
var RM=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var els=document.querySelectorAll(".reveal,.card,.era-chip,.mind-branch,.story-card,.warn-box,.step");
if(!RM&&"IntersectionObserver" in window){els.forEach(function(e){e.classList.add("rv")});
 var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add("in");io.unobserve(en.target)}})},{rootMargin:"0px 0px -8% 0px"});
 els.forEach(function(e){io.observe(e)});}
function count(el){var to=+el.dataset.to;if(RM){el.textContent=to;return}var t0=null;function f(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/1200);el.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
var cs=document.querySelectorAll(".counter");if("IntersectionObserver" in window){var co=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){count(en.target);co.unobserve(en.target)}})});cs.forEach(function(c){co.observe(c)})}
var fg="all",fa="all",grid=document.getElementById("book-grid"),cnt=document.getElementById("lib-count");
function apply(){if(!grid)return;var n=0;grid.querySelectorAll(".book").forEach(function(b){var ok=(fg==="all"||b.dataset.g===fg)&&(fa==="all"||b.dataset.a.split(" ").indexOf(fa)>=0);b.hidden=!ok;if(ok)n++});if(cnt)cnt.textContent="显示 "+n+" 本"}
document.querySelectorAll(".lf").forEach(function(btn){btn.addEventListener("click",function(){var k=btn.dataset.fg?"fg":"fa";document.querySelectorAll(".lf[data-"+k+"]").forEach(function(x){x.classList.remove("on")});btn.classList.add("on");if(k==="fg")fg=btn.dataset.fg;else fa=btn.dataset.fa;apply()})});apply();
var tb=document.getElementById("book-table");if(tb){tb.querySelectorAll("th").forEach(function(th,i){if(i>3)return;th.style.cursor="pointer";var asc=true;th.addEventListener("click",function(){var body=tb.tBodies[0],rows=[].slice.call(body.rows);rows.sort(function(a,b){var x=a.cells[i],y=b.cells[i];var vx=x.dataset.v!==undefined?+x.dataset.v:x.textContent,vy=y.dataset.v!==undefined?+y.dataset.v:y.textContent;var r=typeof vx==="number"?vx-vy:vx.localeCompare(vy,"zh");return asc?r:-r});asc=!asc;rows.forEach(function(r){body.appendChild(r)})})})}
var st=document.getElementById("stepper");if(st){var tabs=st.querySelectorAll(".st-tab"),ps=st.querySelectorAll(".st-panel"),fill=document.getElementById("st-fill"),play=document.getElementById("st-play"),i=0,timer=null;
 function go(n){i=(n+3)%3;tabs.forEach(function(t,k){t.classList.toggle("on",k===i);t.setAttribute("aria-selected",k===i)});ps.forEach(function(p,k){p.classList.toggle("on",k===i)});fill.style.width=((i+1)/3*100)+"%"}
 function start(){stop();timer=setInterval(function(){go(i+1)},3500);play.textContent="⏸ 暂停"}function stop(){if(timer)clearInterval(timer);timer=null;play.textContent="▶ 播放"}
 tabs.forEach(function(t){t.addEventListener("click",function(){stop();go(+t.dataset.i)})});
 document.getElementById("st-prev").onclick=function(){stop();go(i-1)};document.getElementById("st-next").onclick=function(){stop();go(i+1)};play.onclick=function(){timer?stop():start()};
 go(0);if(RM)stop();else start();}
document.querySelectorAll(".flip").forEach(function(f){f.addEventListener("click",function(){f.classList.toggle("on")})});
})();
