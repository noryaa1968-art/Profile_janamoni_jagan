/**
 * portfolio/static/js/main.js
 * Handles: theme toggle, navbar scroll, mobile menu,
 *          smooth scroll, typing effect, scroll reveal,
 *          project filter, contact form, back-to-top.
 */

/* ══════════════════════════════════════════════════════════════
   1. THEME TOGGLE  (persisted via localStorage)
══════════════════════════════════════════════════════════════ */
(function initTheme() {
  const html       = document.documentElement;
  const btn        = document.getElementById('themeToggle');
  const iconMoon   = document.getElementById('iconMoon');
  const iconSun    = document.getElementById('iconSun');

  const saved = localStorage.getItem('theme') || 'dark';
  applyTheme(saved);

  btn.addEventListener('click', () => {
    const next = html.dataset.theme === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    localStorage.setItem('theme', next);
  });

  function applyTheme(t) {
    html.dataset.theme = t;
    if (t === 'light') {
      iconMoon.style.display = 'none';
      iconSun.style.display  = 'block';
    } else {
      iconMoon.style.display = 'block';
      iconSun.style.display  = 'none';
    }
  }
})();


/* ══════════════════════════════════════════════════════════════
   2. NAVBAR – scroll shadow + active link highlighting
══════════════════════════════════════════════════════════════ */
(function initNavbar() {
  const navbar  = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-links .nav-link');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  function onScroll() {
    // Scrolled class for background blur
    navbar.classList.toggle('scrolled', window.scrollY > 20);

    // Active section highlighting
    let current = '';
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
    });
    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
    });
  }
})();


/* ══════════════════════════════════════════════════════════════
   3. MOBILE MENU
══════════════════════════════════════════════════════════════ */
(function initMobileMenu() {
  const btn  = document.getElementById('hamburger');
  const menu = document.getElementById('mobileMenu');
  const mobileLinks = document.querySelectorAll('[data-mobile]');

  btn.addEventListener('click', toggle);
  mobileLinks.forEach(link => link.addEventListener('click', close));

  function toggle() {
    const isOpen = menu.classList.toggle('open');
    btn.classList.toggle('open', isOpen);
    btn.setAttribute('aria-expanded', isOpen);
    menu.setAttribute('aria-hidden', !isOpen);
  }
  function close() {
    menu.classList.remove('open');
    btn.classList.remove('open');
    btn.setAttribute('aria-expanded', false);
    menu.setAttribute('aria-hidden', true);
  }
})();


/* ══════════════════════════════════════════════════════════════
   4. TYPING EFFECT
══════════════════════════════════════════════════════════════ */
(function initTyping() {
  const target = document.getElementById('typingTarget');
  if (!target) return;

  const phrases = [
    'Python Full-Stack Developer',
    'AI / ML Enthusiast',
    'LangChain & RAG Builder',
    'Open Source Contributor',
  ];

  let phraseIdx = 0;
  let charIdx   = 0;
  let deleting  = false;
  const SPEED_TYPE = 70;
  const SPEED_DEL  = 35;
  const PAUSE      = 2000;

  function tick() {
    const phrase = phrases[phraseIdx];
    target.textContent = deleting
      ? phrase.slice(0, charIdx--)
      : phrase.slice(0, charIdx++);

    if (!deleting && charIdx > phrase.length) {
      deleting = true;
      setTimeout(tick, PAUSE);
      return;
    }
    if (deleting && charIdx < 0) {
      deleting  = false;
      charIdx   = 0;
      phraseIdx = (phraseIdx + 1) % phrases.length;
    }
    setTimeout(tick, deleting ? SPEED_DEL : SPEED_TYPE);
  }

  // Small initial delay so the page has loaded visually
  setTimeout(tick, 800);
})();


/* ══════════════════════════════════════════════════════════════
   5. SCROLL REVEAL (Intersection Observer)
══════════════════════════════════════════════════════════════ */
(function initReveal() {
  const els = document.querySelectorAll('.reveal');
  if (!els.length) return;

  const observer = new IntersectionObserver(
    entries => entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);   // animate once
      }
    }),
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  els.forEach(el => observer.observe(el));
})();


/* ══════════════════════════════════════════════════════════════
   6. PROJECT FILTER
══════════════════════════════════════════════════════════════ */
(function initFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards      = document.querySelectorAll('.project-card');
  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;
      cards.forEach(card => {
        const match = filter === 'all' || card.dataset.category === filter;
        card.classList.toggle('hidden', !match);
      });
    });
  });
})();


/* ══════════════════════════════════════════════════════════════
   7. CONTACT FORM
══════════════════════════════════════════════════════════════ */
(function initContactForm() {
  const form      = document.getElementById('contactForm');
  const toast     = document.getElementById('formToast');
  const submitBtn = document.getElementById('submitBtn');
  if (!form) return;

  // Live validation helpers
  const rules = {
    name:    { el: 'name',    errId: 'nameError',    test: v => v.trim().length >= 2,  msg: 'Name must be at least 2 characters.' },
    email:   { el: 'email',   errId: 'emailError',   test: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()), msg: 'Enter a valid email address.' },
    subject: { el: 'subject', errId: 'subjectError', test: v => v.trim().length >= 3,  msg: 'Subject must be at least 3 characters.' },
    message: { el: 'message', errId: 'messageError', test: v => v.trim().length >= 10, msg: 'Message must be at least 10 characters.' },
  };

  // Attach blur validation to each field
  Object.values(rules).forEach(({ el, errId, test, msg }) => {
    const input = document.getElementById(el);
    const errEl = document.getElementById(errId);
    input.addEventListener('blur', () => {
      const valid = test(input.value);
      input.classList.toggle('error', !valid);
      errEl.textContent = valid ? '' : msg;
    });
    input.addEventListener('input', () => {
      if (input.classList.contains('error') && test(input.value)) {
        input.classList.remove('error');
        errEl.textContent = '';
      }
    });
  });

  form.addEventListener('submit', async e => {
    e.preventDefault();

    // Full client-side validation pass
    let hasError = false;
    Object.values(rules).forEach(({ el, errId, test, msg }) => {
      const input = document.getElementById(el);
      const errEl = document.getElementById(errId);
      if (!test(input.value)) {
        input.classList.add('error');
        errEl.textContent = msg;
        hasError = true;
      }
    });
    if (hasError) return;

    // Loading state
    submitBtn.classList.add('loading');
    submitBtn.disabled = true;
    hideToast();

    try {
      const res = await fetch('/contact', {
        method: 'POST',
        body: new FormData(form),
      });
      const data = await res.json();

      if (data.success) {
        showToast('success', data.message || 'Message sent! I\'ll be in touch soon.');
        form.reset();
      } else if (data.errors) {
        // Show server-side field errors
        Object.entries(data.errors).forEach(([field, msg]) => {
          const input = document.getElementById(field);
          const errEl = document.getElementById(field + 'Error');
          if (input && errEl) {
            input.classList.add('error');
            errEl.textContent = msg;
          }
        });
      } else {
        showToast('error', data.error || 'Something went wrong. Please try again.');
      }
    } catch {
      showToast('error', 'Network error. Please check your connection and try again.');
    } finally {
      submitBtn.classList.remove('loading');
      submitBtn.disabled = false;
    }
  });

  function showToast(type, msg) {
    toast.textContent = msg;
    toast.className   = `form-toast ${type}`;
    toast.style.display = 'block';
    setTimeout(hideToast, 8000);
  }
  function hideToast() {
    toast.className   = 'form-toast';
    toast.style.display = 'none';
  }
})();


/* ══════════════════════════════════════════════════════════════
   8. BACK TO TOP
══════════════════════════════════════════════════════════════ */
(function initBackToTop() {
  const btn = document.getElementById('backToTop');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();


/* ══════════════════════════════════════════════════════════════
   9. FOOTER YEAR
══════════════════════════════════════════════════════════════ */
(function setYear() {
  const el = document.getElementById('footerYear');
  if (el) el.textContent = new Date().getFullYear();
})();
