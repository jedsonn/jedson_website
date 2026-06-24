/* ============================================================================
   jedson_website — engagement widget (likes / flags / comments / suggestions)
   Backend: Supabase project "rumo", tables web_reactions (public like counts)
   and web_feedback (PRIVATE — only Jedson reads, in the Supabase dashboard).
   Loaded after the supabase-js CDN script. Degrades silently if unavailable.
   ============================================================================ */
(function () {
  "use strict";
  var SB_URL = "https://nmkbznbjgfuqopezfncs.supabase.co";
  var SB_KEY = "sb_publishable_NuyK_vdjUJnxNPfOww8XNw_fsZ84bk0";

  if (!window.supabase || !window.supabase.createClient) return; // CDN failed → no-op
  var sb;
  try { sb = window.supabase.createClient(SB_URL, SB_KEY); } catch (e) { return; }

  var PAGE = (location.pathname.split("/").pop() || "index").replace(/\.html$/, "") || "index";
  var clientId = localStorage.getItem("web_cid");
  if (!clientId) { clientId = "c_" + Math.random().toString(36).slice(2) + Date.now().toString(36); localStorage.setItem("web_cid", clientId); }

  function hashId(s) { var h = 5381; s = s || ""; for (var i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) >>> 0; return "p" + h.toString(36); }
  function esc(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function likedKey(pid) { return "web_liked_" + PAGE + "_" + pid; }
  function liked(pid) { return localStorage.getItem(likedKey(pid)) === "1"; }
  function setLiked(pid) { localStorage.setItem(likedKey(pid), "1"); }

  function sendFeedback(kind, extra) {
    var p = { kind: kind, page: PAGE, user_agent: (navigator.userAgent || "").slice(0, 400) };
    for (var k in (extra || {})) p[k] = extra[k];
    return sb.from("web_feedback").insert(p).then(function (r) { return !r.error; }).catch(function () { return false; });
  }

  // ---- styles ----
  var css = document.createElement("style");
  css.textContent =
  ".wr-bar{display:flex;align-items:center;gap:16px;margin-top:8px;padding-top:7px;border-top:1px solid rgba(255,255,255,.06);flex-wrap:wrap;}" +
  ".wr-btn{font-family:inherit;font-size:11px;font-weight:500;line-height:1;display:inline-flex;align-items:center;gap:4px;background:none;border:none;color:#5a6075;padding:2px 0;cursor:pointer;transition:color .15s;}" +
  ".wr-btn:hover{color:#9298ab;}" +
  ".wr-like.on{color:#5b9bf5;}" +
  ".wr-cnt{font-variant-numeric:tabular-nums;}" +
  ".wr-msg{font-size:11px;color:#5bca7b;}" +
  ".wr-form{margin-top:8px;display:flex;flex-direction:column;gap:6px;}" +
  ".wr-form[hidden]{display:none !important;}" +
  ".wr-form textarea{width:100%;min-height:62px;background:#0c0e13;border:1px solid rgba(255,255,255,.18);border-radius:8px;color:#dfe1e8;padding:8px;font:inherit;font-size:13px;resize:vertical;}" +
  ".wr-form input{background:#0c0e13;border:1px solid rgba(255,255,255,.18);border-radius:8px;color:#dfe1e8;padding:7px 8px;font:inherit;font-size:12.5px;}" +
  ".wr-row{display:flex;gap:8px;align-items:center;}" +
  ".wr-send{background:#5b9bf5;border:none;color:#04122a;font-weight:600;padding:7px 14px;border-radius:8px;cursor:pointer;font:inherit;font-size:12.5px;}" +
  ".wr-cancel{background:transparent;border:1px solid rgba(255,255,255,.2);color:#9298ab;padding:7px 12px;border-radius:8px;cursor:pointer;font:inherit;font-size:12.5px;}" +
  /* floating suggestion button + panel + toast (work on light or dark pages) */
  ".wr-fab{position:fixed;right:18px;bottom:18px;z-index:99998;background:#1a5276;color:#fff;border:none;border-radius:999px;padding:12px 18px;font-family:system-ui,-apple-system,sans-serif;font-size:13px;font-weight:600;box-shadow:0 6px 20px rgba(0,0,0,.25);cursor:pointer;}" +
  ".wr-fab:hover{filter:brightness(1.08);}" +
  ".wr-panel{position:fixed;right:18px;bottom:70px;z-index:99999;width:330px;max-width:calc(100vw - 36px);background:#fff;color:#1a1c22;border:1px solid #e2e4e0;border-radius:14px;box-shadow:0 18px 50px rgba(0,0,0,.28);padding:16px 16px 14px;font-family:system-ui,-apple-system,sans-serif;}" +
  ".wr-panel h4{margin:0 0 3px;font-size:15px;font-weight:600;}" +
  ".wr-panel p{margin:0 0 10px;font-size:12.5px;color:#586068;line-height:1.45;}" +
  ".wr-panel textarea{width:100%;min-height:92px;border:1px solid #d7dad6;border-radius:9px;padding:9px;font:inherit;font-size:13px;resize:vertical;color:#1a1c22;box-sizing:border-box;}" +
  ".wr-panel input{width:100%;border:1px solid #d7dad6;border-radius:9px;padding:8px 9px;margin-top:8px;font:inherit;font-size:13px;color:#1a1c22;box-sizing:border-box;}" +
  ".wr-actions{display:flex;gap:8px;margin-top:11px;justify-content:flex-end;}" +
  ".wr-psend{background:#1a5276;color:#fff;border:none;padding:8px 16px;border-radius:9px;font:600 13px system-ui;cursor:pointer;}" +
  ".wr-pcancel{background:#f0eeea;color:#586068;border:none;padding:8px 14px;border-radius:9px;font:13px system-ui;cursor:pointer;}" +
  ".wr-toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%);z-index:100000;background:#1a1c22;color:#fff;padding:10px 16px;border-radius:10px;font:13px system-ui;box-shadow:0 8px 24px rgba(0,0,0,.3);opacity:0;transition:opacity .25s;pointer-events:none;max-width:90vw;text-align:center;}" +
  ".wr-toast.show{opacity:1;}";
  document.head.appendChild(css);

  // ---- toast ----
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "wr-toast"; document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toast._t); toast._t = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }

  // ---- per-paper reactions (Map timeline cards: .c with a .ti title) ----
  var cards = document.querySelectorAll(".c");
  if (cards.length) {
    cards.forEach(function (card) {
      var titleEl = card.querySelector(".ti");
      if (!titleEl) return;
      var title = titleEl.textContent.trim();
      var pid = hashId(title + "|" + (card.dataset.sub || ""));

      var bar = document.createElement("div");
      bar.className = "wr-bar";
      bar.innerHTML =
        '<button type="button" class="wr-btn wr-like' + (liked(pid) ? " on" : "") + '" data-pid="' + pid + '" title="Like this paper">&#9829; <span class="wr-cnt">0</span></button>' +
        '<button type="button" class="wr-btn wr-flag" title="Flag for Jedson to review">&#9873; Flag</button>' +
        '<button type="button" class="wr-btn wr-cmt" title="Leave a private comment for Jedson">&#128172; Comment</button>' +
        '<span class="wr-msg"></span>';

      var form = document.createElement("div");
      form.className = "wr-form";
      form.hidden = true;
      form.innerHTML =
        '<textarea maxlength="5000" placeholder="A private note to Jedson about this paper…"></textarea>' +
        '<div class="wr-row"><input type="text" maxlength="200" placeholder="Your email (optional)"><button type="button" class="wr-send">Send</button><button type="button" class="wr-cancel">Cancel</button></div>';

      card.appendChild(bar);
      card.appendChild(form);

      // stop the Map's whole-card expand toggle from firing on our controls
      function stop(e) { e.stopPropagation(); }
      bar.addEventListener("click", stop);
      form.addEventListener("click", stop);

      var likeBtn = bar.querySelector(".wr-like");
      var cntEl = bar.querySelector(".wr-cnt");
      var msgEl = bar.querySelector(".wr-msg");

      likeBtn.addEventListener("click", function (e) {
        stop(e);
        if (liked(pid)) { return; }
        setLiked(pid); likeBtn.classList.add("on");
        cntEl.textContent = (parseInt(cntEl.textContent, 10) || 0) + 1;
        sb.from("web_reactions").insert({ page: PAGE, paper_id: pid, client_id: clientId }).then(function () {});
      });

      bar.querySelector(".wr-flag").addEventListener("click", function (e) {
        stop(e);
        sendFeedback("flag", { paper_id: pid, paper_title: title.slice(0, 400) });
        msgEl.textContent = "Flagged — thanks!";
        setTimeout(function () { msgEl.textContent = ""; }, 2600);
      });

      bar.querySelector(".wr-cmt").addEventListener("click", function (e) {
        stop(e); form.hidden = !form.hidden; if (!form.hidden) form.querySelector("textarea").focus();
      });
      form.querySelector(".wr-cancel").addEventListener("click", function (e) { stop(e); form.hidden = true; });
      form.querySelector(".wr-send").addEventListener("click", function (e) {
        stop(e);
        var body = form.querySelector("textarea").value.trim();
        if (!body) { form.querySelector("textarea").focus(); return; }
        var contact = form.querySelector("input").value.trim();
        sendFeedback("comment", { paper_id: pid, paper_title: title.slice(0, 400), body: body, contact: contact });
        form.querySelector("textarea").value = ""; form.querySelector("input").value = ""; form.hidden = true;
        toast("Comment sent to Jedson — thank you!");
      });
    });

    // load like counts for this page
    sb.from("web_reactions").select("paper_id").eq("page", PAGE).limit(20000).then(function (r) {
      if (r.error || !r.data) return;
      var counts = {};
      r.data.forEach(function (row) { counts[row.paper_id] = (counts[row.paper_id] || 0) + 1; });
      document.querySelectorAll(".wr-like").forEach(function (b) {
        b.querySelector(".wr-cnt").textContent = counts[b.getAttribute("data-pid")] || 0;
      });
    });
  }

  // ---- floating Suggestions / requests box (every page) ----
  var fab = document.createElement("button");
  fab.type = "button"; fab.className = "wr-fab"; fab.textContent = "💡 Suggest / request";
  var panel = null;
  fab.addEventListener("click", function () {
    if (panel) { panel.remove(); panel = null; return; }
    panel = document.createElement("div");
    panel.className = "wr-panel";
    panel.innerHTML =
      "<h4>Suggest a paper or send a note</h4>" +
      "<p>Requests, missing papers, corrections, or anything else — goes straight to Jedson (private).</p>" +
      '<textarea maxlength="5000" placeholder="Your suggestion or request…"></textarea>' +
      '<input type="text" maxlength="200" placeholder="Your email (optional, if you’d like a reply)">' +
      '<div class="wr-actions"><button type="button" class="wr-pcancel">Close</button><button type="button" class="wr-psend">Send</button></div>';
    document.body.appendChild(panel);
    panel.querySelector("textarea").focus();
    panel.querySelector(".wr-pcancel").addEventListener("click", function () { panel.remove(); panel = null; });
    panel.querySelector(".wr-psend").addEventListener("click", function () {
      var body = panel.querySelector("textarea").value.trim();
      if (!body) { panel.querySelector("textarea").focus(); return; }
      var contact = panel.querySelector("input").value.trim();
      sendFeedback("suggestion", { body: body, contact: contact });
      panel.remove(); panel = null;
      toast("Sent to Jedson — thank you!");
    });
  });
  document.body.appendChild(fab);
})();
