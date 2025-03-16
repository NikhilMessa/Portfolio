(function (C, A, L) { 
    let p = function (a, ar) { a.q.push(ar); }; 
    let d = C.document; 
    C.Cal = C.Cal || function () { 
      let cal = C.Cal; 
      let ar = arguments; 
      if (!cal.loaded) { 
        cal.ns = {}; 
        cal.q = cal.q || []; 
        let script = d.createElement("script"); 
        script.src = A; 
        script.async = true; 
        d.head.appendChild(script); 
        cal.loaded = true; 
      } 
      if (ar[0] === L) { 
        const api = function () { p(api, arguments); }; 
        const namespace = ar[1]; 
        api.q = api.q || []; 
        if (typeof namespace === "string") { 
          cal.ns[namespace] = cal.ns[namespace] || api; 
          p(cal.ns[namespace], ar); 
          p(cal, ["initNamespace", namespace]); 
        } else p(cal, ar); 
        return; 
      } 
      p(cal, ar); 
    }; 
  })(window, "https://app.cal.com/embed/embed.js", "init");
  Cal("init", "15min", { origin: "https://cal.com" });
  Cal.ns["15min"]("ui", { 
    "hideEventTypeDetails": false,
    "layout": "month_view"
  });
  document.addEventListener("DOMContentLoaded", function() {
    const bookNowButton = document.getElementById("bookNowBtn");
    if (bookNowButton) {
      bookNowButton.addEventListener("click", function() {
        const calLink = document.getElementById("cal-link");
        if (calLink) {
          calLink.click();
        } else {
          alert("Booking link not found!");
        }
      });
    } else {
      console.error("Book Now button not found!");
    }
  });