
(function(){
  window.toggleMenu=function(){document.querySelector('nav.main').classList.toggle('open')};
  var imgs=[].slice.call(document.querySelectorAll('.gal img'));
  if(!imgs.length) return;
  var lb=document.createElement('div'); lb.id='lb';
  lb.innerHTML='<button class="close">Fermer ✕</button><button class="nav prev">‹</button><img alt=""><button class="nav next">›</button><div class="cnt"></div>';
  document.body.appendChild(lb);
  var big=lb.querySelector('img'),cnt=lb.querySelector('.cnt'),i=0;
  function show(n){i=(n+imgs.length)%imgs.length;big.src=imgs[i].src;cnt.textContent=(i+1)+' / '+imgs.length;}
  function open(n){show(n);lb.classList.add('open');document.body.style.overflow='hidden';}
  function close(){lb.classList.remove('open');document.body.style.overflow='';}
  imgs.forEach(function(im,n){im.addEventListener('click',function(){open(n)});});
  lb.querySelector('.close').onclick=close; big.onclick=close;
  lb.querySelector('.prev').onclick=function(e){e.stopPropagation();show(i-1)};
  lb.querySelector('.next').onclick=function(e){e.stopPropagation();show(i+1)};
  lb.addEventListener('click',function(e){if(e.target===lb)close()});
  document.addEventListener('keydown',function(e){
    if(!lb.classList.contains('open'))return;
    if(e.key==='Escape')close(); if(e.key==='ArrowRight')show(i+1); if(e.key==='ArrowLeft')show(i-1);
  });
})();
