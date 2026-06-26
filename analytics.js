/* ============================================================================
   Site analytics — Google Analytics 4 (GA4)
   ----------------------------------------------------------------------------
   ONE step to turn this on: paste your GA4 Measurement ID below (it looks like
   G-XXXXXXXXXX), commit, and you're live. Every page already loads this file,
   so this is the only place you ever edit.

   Get the ID: analytics.google.com → Admin → create a Web data stream for
   https://www.jedsonpinto.com → copy the "Measurement ID".

   Until a valid ID is set, this file does nothing (no tracking, no errors).
   ============================================================================ */
(function () {
  "use strict";

  var GA_ID = "G-TK1JTN1R3M"; // GA4 Measurement ID for www.jedsonpinto.com

  // Do nothing until a real ID is provided, or if the visitor asked not to be tracked.
  if (!GA_ID || GA_ID.indexOf("G-") !== 0) return;
  if (navigator.doNotTrack === "1" || window.doNotTrack === "1") return;

  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_ID);
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag("js", new Date());
  gtag("config", GA_ID);

  /* Rich click tracking — fires a "link_click" event with a readable label and a
     type (outbound | pdf | cv_pdf | email), so you can see which papers, your CV,
     and external profiles get clicked. Complements GA4's built-in measurement. */
  document.addEventListener("click", function (e) {
    var a = e.target && e.target.closest ? e.target.closest("a[href]") : null;
    if (!a || typeof window.gtag !== "function") return;
    var url;
    try { url = new URL(a.href, location.href); } catch (_) { return; }
    var type = null;
    if (url.protocol === "mailto:") type = "email";
    else if (url.protocol === "http:" || url.protocol === "https:") {
      if (/\.pdf($|\?)/i.test(url.pathname)) type = /cv/i.test(url.pathname) ? "cv_pdf" : "pdf";
      else if (url.host !== location.host) type = "outbound";
    }
    if (!type) return; // ignore internal page-to-page nav (page_view already covers it)
    window.gtag("event", "link_click", {
      link_type: type,
      link_text: (a.textContent || "").trim().slice(0, 100),
      link_url: url.href.slice(0, 300),
      link_domain: url.host
    });
  }, true);
})();
