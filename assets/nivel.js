// Widget didactic: butonul care dezvaluie nivelul interfetei.
// Folosire: <script src="../../assets/nivel.js" data-nivel="2"></script>  (1, 2, 3 sau 4)
(function () {
  var NIVELE = {
    1: ['Nivelul 1 din 4 – Nu merge', 'doesn’t work', 'Sarcina se realizează greu sau deloc: lipsesc mesajele, butoanele nu sunt clare, erorile nu sunt explicate.'],
    2: ['Nivelul 2 din 4 – Merge', 'works', 'Aplicația își face treaba, dar este neintuitivă, inconsecventă sau nu se adaptează la ecrane mici.'],
    3: ['Nivelul 3 din 4 – Merge bine', 'works well', 'Interfață clară și consecventă, cu feedback pentru fiecare acțiune, mesaje utile și aranjare responsivă.'],
    4: ['Nivelul 4 din 4 – Merge foarte bine', 'works very well', 'În plus: accesibilitate, prevenirea erorilor, navigare cu tastatura și detalii de finețe.'],
  };
  var script = document.currentScript;
  var n = parseInt(script.getAttribute('data-nivel'), 10) || 1;
  var info = NIVELE[n];
  var css = document.createElement('link');
  css.rel = 'stylesheet';
  css.href = script.src.replace(/nivel\.js(\?.*)?$/, 'nivel.css');
  document.head.appendChild(css);

  function init() {
    var box = document.createElement('div');
    box.className = 'nivel-widget';
    box.innerHTML =
      '<button type="button" aria-expanded="false" aria-controls="nivel-panel">Ce nivel are această interfață?</button>' +
      '<div class="nivel-panel" id="nivel-panel" hidden>' +
      '<strong class="n' + n + '">' + info[0] + ' <em>(' + info[1] + ')</em></strong>' +
      '<p>' + info[2] + '</p>' +
      '<p>Comparați cu celelalte variante și cu fișa de lucru (<a href="../FISA.pdf">FISA.pdf</a>).</p></div>';
    document.body.appendChild(box);
    var btn = box.querySelector('button');
    var panel = box.querySelector('.nivel-panel');
    btn.addEventListener('click', function () {
      var deschis = panel.hidden;
      panel.hidden = !deschis;
      btn.setAttribute('aria-expanded', String(deschis));
      btn.textContent = deschis ? 'Ascunde nivelul' : 'Ce nivel are această interfață?';
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
