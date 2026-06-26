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

  var GA_ID = ""; // <-- paste your GA4 Measurement ID here, e.g. "G-ABC1234XYZ"

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
})();
