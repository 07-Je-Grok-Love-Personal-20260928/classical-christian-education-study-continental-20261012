/* CCE v20261012-3: reveal, counters, library filter, sort, stepper, flip */
(function(){"use strict";
var RM=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var els=document.querySelectorAll(".reveal:not(.book),.card,.era-chip,.mind-branch,.story-card,.warn-box,.step");
if(!RM&&"IntersectionObserver" in window){els.forEach(function(e){e.classList.add("rv")});
 var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add("in");io.unobserve(en.target)}})},{rootMargin:"0px 0px -8% 0px"});
 els.forEach(function(e){io.observe(e)});setTimeout(function(){els.forEach(function(e){var r=e.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)e.classList.add("in")})},1500);}
function count(el){var to=+el.dataset.to;if(RM){el.textContent=to;return}var t0=null;function f(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/1200);el.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
var cs=document.querySelectorAll(".counter");if("IntersectionObserver" in window){var co=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){count(en.target);co.unobserve(en.target)}})});cs.forEach(function(c){co.observe(c)})}
var F={g:"all",a:"all",z:"all",t:"all",q:""},PAGE=12,shown=PAGE,grid=document.getElementById("book-grid"),cnt=document.getElementById("lib-count"),more=document.getElementById("lib-more");
function apply(reset){if(!grid)return;if(reset)shown=PAGE;var m=[],q=F.q.toLowerCase();grid.querySelectorAll(".book").forEach(function(b){var ok=(F.g==="all"||b.dataset.g===F.g)&&(F.a==="all"||b.dataset.a.split(" ").indexOf(F.a)>=0)&&(F.z==="all"||b.dataset.zh===F.z)&&(F.t==="all"||b.dataset.t===F.t)&&(!q||b.dataset.s.toLowerCase().indexOf(q)>=0);b.hidden=true;if(ok)m.push(b)});m.forEach(function(b,i){if(i<shown)b.hidden=false});if(cnt)cnt.textContent="符合 "+m.length+" 本，显示 "+Math.min(shown,m.length)+" 本";if(more){more.hidden=shown>=m.length;more.textContent="加载更多（还有 "+Math.max(0,m.length-shown)+" 本）"}}
document.querySelectorAll(".lf").forEach(function(btn){btn.addEventListener("click",function(){var k=["fg","fa","fz","ft"].filter(function(x){return btn.dataset[x]!==undefined})[0];document.querySelectorAll(".lf[data-"+k+"]").forEach(function(x){x.classList.remove("on")});btn.classList.add("on");F[k.slice(1)]=btn.dataset[k];apply(true)})});
var se=document.getElementById("lib-search"),st0;if(se)se.addEventListener("input",function(){clearTimeout(st0);st0=setTimeout(function(){F.q=se.value.trim();apply(true)},150)});
if(more)more.addEventListener("click",function(){shown+=PAGE;apply(false)});
document.querySelectorAll(".vt").forEach(function(v){v.addEventListener("click",function(){document.querySelectorAll(".vt").forEach(function(x){x.classList.remove("on")});v.classList.add("on");grid.classList.toggle("list",v.dataset.v==="list")})});
document.addEventListener("click",function(e){var t=e.target.closest(".tc-btn");if(!t)return;var tr=t.closest(".bk-toc,.toc-panel").querySelectorAll(".tree details");tr.forEach(function(d){d.open=t.dataset.tc==="open"})});
function hdrOff(){var h=document.querySelector(".site-header");return (h?h.getBoundingClientRect().height:0)+12}
function goBook(id,push){var el=document.getElementById(id);if(!el||!el.classList.contains("book"))return false;if(el.hidden){F={g:"all",a:"all",z:"all",t:"all",q:""};document.querySelectorAll(".lf").forEach(function(x){x.classList.toggle("on",Object.values(x.dataset)[0]==="all")});if(se)se.value="";var all=[].slice.call(grid.querySelectorAll(".book"));shown=Math.max(PAGE,Math.ceil((all.indexOf(el)+1)/PAGE)*PAGE);apply(false)}
 var tc=el.querySelector(".bk-toc .tree");if(tc)[].forEach.call(tc.children,function(li){var d=li.querySelector(":scope>details");if(d)d.open=true});
 if(push&&location.hash!=="#"+id)history.pushState(null,"","#"+id);
 requestAnimationFrame(function(){var y=el.getBoundingClientRect().top+window.pageYOffset-hdrOff();window.scrollTo({top:y,behavior:RM?"auto":"smooth"})});
 el.classList.remove("bk-hl");void el.offsetWidth;el.classList.add("bk-hl");setTimeout(function(){el.classList.remove("bk-hl")},2400);return true}
document.querySelectorAll(".spine").forEach(function(sp){sp.addEventListener("click",function(e){if(goBook(sp.getAttribute("href").slice(1),true))e.preventDefault()})});
function onHash(){var h=decodeURIComponent(location.hash.slice(1));if(/^bk-/.test(h))goBook(h,false)}
window.addEventListener("popstate",onHash);window.addEventListener("hashchange",onHash);
setTimeout(onHash,0);
apply(true);
var tb=document.getElementById("book-table");if(tb){tb.querySelectorAll("th").forEach(function(th,i){if(i>6)return;th.style.cursor="pointer";var asc=true;th.addEventListener("click",function(){var body=tb.tBodies[0],rows=[].slice.call(body.rows);rows.sort(function(a,b){var x=a.cells[i],y=b.cells[i];var vx=x.dataset.v!==undefined?+x.dataset.v:x.textContent,vy=y.dataset.v!==undefined?+y.dataset.v:y.textContent;var r=typeof vx==="number"?vx-vy:vx.localeCompare(vy,"zh");return asc?r:-r});asc=!asc;rows.forEach(function(r){body.appendChild(r)})})})}
var st=document.getElementById("stepper");if(st){var tabs=st.querySelectorAll(".st-tab"),ps=st.querySelectorAll(".st-panel"),fill=document.getElementById("st-fill"),play=document.getElementById("st-play"),i=0,timer=null;
 function go(n){i=(n+3)%3;tabs.forEach(function(t,k){t.classList.toggle("on",k===i);t.setAttribute("aria-selected",k===i)});ps.forEach(function(p,k){p.classList.toggle("on",k===i)});fill.style.width=((i+1)/3*100)+"%"}
 function start(){stop();timer=setInterval(function(){go(i+1)},3500);play.textContent="⏸ 暂停"}function stop(){if(timer)clearInterval(timer);timer=null;play.textContent="▶ 播放"}
 tabs.forEach(function(t){t.addEventListener("click",function(){stop();go(+t.dataset.i)})});
 document.getElementById("st-prev").onclick=function(){stop();go(i-1)};document.getElementById("st-next").onclick=function(){stop();go(i+1)};play.onclick=function(){timer?stop():start()};
 go(0);if(RM)stop();else start();}
document.querySelectorAll(".flip").forEach(function(f){f.addEventListener("click",function(){f.classList.toggle("on")})});
/* donut/bars animate */
document.querySelectorAll(".donut,.sc-bar").forEach(function(e){if(RM||!("IntersectionObserver" in window)){e.classList.add("go");return}var o=new IntersectionObserver(function(es){if(es[0].isIntersecting){e.classList.add("go");o.disconnect()}});o.observe(e)});
})();
