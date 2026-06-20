/**
 * JLPT N5 Essential Cheat Sheet - Interactive Logic & Print Controller
 * Designed for optimal revision and seamless browser PDF export.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  lucide.createIcons();

  // State Variables
  let currentSlide = 1;
  let isPdfMode = false;
  const body = document.body;
  const slides = document.querySelectorAll('.slide');
  let totalSlides = slides.length;
  const currentSlideNumEl = document.getElementById('currentSlideNum');
  const totalSlidesNumEl = document.getElementById('totalSlidesNum');
  
  if (totalSlidesNumEl) {
    totalSlidesNumEl.textContent = totalSlides;
  }

  const progressFill = document.getElementById('progressFill');
  const searchInput = document.getElementById('vocabSearch');
  const clearSearchBtn = document.getElementById('clearSearch');
  
  // Navigation Buttons
  const prevBtn = document.getElementById('prevSlideBtn');
  const nextBtn = document.getElementById('nextSlideBtn');

  // Mode Toggle Elements
  const modeToggleBtn = document.getElementById('modeToggleBtn');
  const modeText = document.getElementById('modeText');
  const modeIcon = document.getElementById('modeIcon');
  const progressBarContainer = document.getElementById('progressBarContainer');

  // Theme Selectors
  const themeBtn = document.getElementById('themeBtn');
  const themeDropdown = document.getElementById('themeDropdown');
  const themeOptions = document.querySelectorAll('.theme-option');

  // Print Action Button
  const printBtn = document.getElementById('printBtn');

  /* ==========================================================================
     SLIDE NAVIGATION STATE
     ========================================================================== */

  function updateSlideDisplay() {
    if (isPdfMode) return; // Disregard active slides in expanded PDF mode

    slides.forEach((slide) => {
      const index = parseInt(slide.getAttribute('data-slide-index'), 10);
      if (index === currentSlide) {
        slide.classList.add('active-slide');
      } else {
        slide.classList.remove('active-slide');
      }
    });

    // Update Indicators
    currentSlideNumEl.textContent = currentSlide;
    const progressPercent = (currentSlide / totalSlides) * 100;
    progressFill.style.width = `${progressPercent}%`;

    // Apply Live Search Filter on newly navigated slide
    applySearchFilter();
  }

  // Quick Navigation Menu Logic
  const jumpButtons = document.querySelectorAll('.jump-btn');
  jumpButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetIndex = parseInt(btn.getAttribute('data-target'), 10);
      if (targetIndex >= 1 && targetIndex <= totalSlides) {
        currentSlide = targetIndex;
        updateSlideDisplay();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });
  });

  function nextSlide() {
    if (currentSlide < totalSlides) {
      currentSlide++;
      updateSlideDisplay();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  function prevSlide() {
    if (currentSlide > 1) {
      currentSlide--;
      updateSlideDisplay();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  // Bind Buttons
  nextBtn.addEventListener('click', nextSlide);
  prevBtn.addEventListener('click', prevSlide);

  // Keyboard Shortcuts
  document.addEventListener('keydown', (e) => {
    if (isPdfMode) return; // Disable slideshow shortcuts in print mode
    
    // Ignore keyboard shortcuts when user is typing in search input
    if (document.activeElement === searchInput) return;

    if (e.key === 'ArrowRight' || e.key === 'Space') {
      e.preventDefault();
      nextSlide();
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      prevSlide();
    }
  });

  /* ==========================================================================
     THEME CONTROLLER
     ========================================================================== */

  // Load Saved Theme
  const savedTheme = localStorage.getItem('n5-cheat-sheet-theme') || 'sakura';
  setTheme(savedTheme);

  // Toggle Theme Dropdown
  themeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    themeDropdown.classList.toggle('show');
  });

  // Close theme dropdown when clicking elsewhere
  document.addEventListener('click', () => {
    themeDropdown.classList.remove('show');
  });

  // Bind Options
  themeOptions.forEach((option) => {
    option.addEventListener('click', () => {
      const selectedTheme = option.getAttribute('data-theme');
      setTheme(selectedTheme);
      themeDropdown.classList.remove('show');
    });
  });

  function setTheme(themeName) {
    // Remove existing themes
    body.classList.remove('theme-sakura', 'theme-matcha', 'theme-fuji', 'theme-sumi');
    
    // Add selected
    body.classList.add(`theme-${themeName}`);
    localStorage.setItem('n5-cheat-sheet-theme', themeName);

    // Update active highlight in dropdown
    themeOptions.forEach((opt) => {
      if (opt.getAttribute('data-theme') === themeName) {
        opt.classList.add('active');
      } else {
        opt.classList.remove('active');
      }
    });
  }

  /* ==========================================================================
     VIEW MODE TOGGLE: SLIDESHOW VS. PRINT REVISION GUIDE
     ========================================================================== */

  modeToggleBtn.addEventListener('click', () => {
    toggleMode();
  });

  function toggleMode() {
    isPdfMode = !isPdfMode;

    if (isPdfMode) {
      // Switch to Revision Guide / PDF Mode
      body.classList.remove('slideshow-mode');
      body.classList.add('pdf-mode');
      
      // Update UI Text & Icons
      modeText.textContent = "Interactive Slides";
      modeIcon.setAttribute('data-lucide', 'presentation');
      
      // Adjust scrollbar configurations
      window.scrollTo({ top: 0 });
    } else {
      // Switch back to Interactive Slideshow
      body.classList.remove('pdf-mode');
      body.classList.add('slideshow-mode');
      
      // Update UI Text & Icons
      modeText.textContent = "Print Guide Mode";
      modeIcon.setAttribute('data-lucide', 'book-open');
      
      // Refresh slides
      updateSlideDisplay();
    }
    
    // Recreate Lucide Icons to render new icons
    lucide.createIcons();
    
    // Run search filter to apply logic appropriately
    applySearchFilter();
  }

  /* ==========================================================================
     LIVE VOCABULARY SEARCH & FILTER
     ========================================================================== */

  searchInput.addEventListener('input', () => {
    if (searchInput.value.trim().length > 0) {
      clearSearchBtn.style.display = 'flex';
    } else {
      clearSearchBtn.style.display = 'none';
    }
    applySearchFilter();
  });

  clearSearchBtn.addEventListener('click', () => {
    searchInput.value = '';
    clearSearchBtn.style.display = 'none';
    searchInput.focus();
    applySearchFilter();
  });

  function applySearchFilter() {
    const query = searchInput.value.toLowerCase().trim();

    // Iterate through all table rows containing vocabulary data
    const rows = document.querySelectorAll('.vocab-row');
    
    rows.forEach((row) => {
      // Extract columns to inspect
      const jpText = row.querySelector('.jp-col') ? row.querySelector('.jp-col').textContent.toLowerCase() : '';
      const romajiText = row.querySelector('.romaji-col') ? row.querySelector('.romaji-col').textContent.toLowerCase() : '';
      const meaningText = row.querySelector('.meaning-col') ? row.querySelector('.meaning-col').textContent.toLowerCase() : '';
      const exampleText = row.querySelector('.example-col') ? row.querySelector('.example-col').textContent.toLowerCase() : '';
      const mnemonicText = row.querySelector('.mnemonic-col') ? row.querySelector('.mnemonic-col').textContent.toLowerCase() : '';
      
      // Match condition
      const isMatch = jpText.includes(query) || 
                      romajiText.includes(query) || 
                      meaningText.includes(query) || 
                      exampleText.includes(query) || 
                      mnemonicText.includes(query);

      // In slideshow mode, we only care about filtering matching rows inside the active slide.
      // In PDF mode, we scan across all slides.
      if (query === '') {
        row.classList.remove('row-hidden');
      } else {
        if (isMatch) {
          row.classList.remove('row-hidden');
        } else {
          row.classList.add('row-hidden');
        }
      }
    });

    // Also search cards in trap sheets or proximity sheets
    const trapCards = document.querySelectorAll('.trap-card');
    trapCards.forEach((card) => {
      if (query === '') {
        card.classList.remove('row-hidden');
        return;
      }
      const cardText = card.textContent.toLowerCase();
      if (cardText.includes(query)) {
        card.classList.remove('row-hidden');
      } else {
        card.classList.add('row-hidden');
      }
    });

    const proximityCards = document.querySelectorAll('.kosado-card');
    proximityCards.forEach((card) => {
      if (query === '') {
        card.classList.remove('row-hidden');
        return;
      }
      const cardText = card.textContent.toLowerCase();
      if (cardText.includes(query)) {
        card.classList.remove('row-hidden');
      } else {
        card.classList.add('row-hidden');
      }
    });

    const grammarCards = document.querySelectorAll('.grammar-card, .conv-card');
    grammarCards.forEach((card) => {
      if (query === '') {
        card.classList.remove('row-hidden');
        return;
      }
      const cardText = card.textContent.toLowerCase();
      if (cardText.includes(query)) {
        card.classList.remove('row-hidden');
      } else {
        card.classList.add('row-hidden');
      }
    });
  }

  /* ==========================================================================
     PRACTICE QUIZ LOGIC
     ========================================================================== */
  
  body.addEventListener('click', (e) => {
    const optionBtn = e.target.closest('.practice-option');
    if (!optionBtn) return;
    
    // Ignore clicks in PDF mode where everything should be visible
    if (isPdfMode) return;
    
    const questionContainer = optionBtn.closest('.practice-question');
    if (!questionContainer) return;
    
    // Check if already answered
    if (questionContainer.classList.contains('answered')) return;
    
    const isCorrect = optionBtn.hasAttribute('data-correct');
    
    // Mark the selected option
    optionBtn.classList.add('selected');
    if (isCorrect) {
      optionBtn.classList.add('correct');
    } else {
      optionBtn.classList.add('incorrect');
      // Highlight the correct one
      const correctOption = questionContainer.querySelector('.practice-option[data-correct]');
      if (correctOption) correctOption.classList.add('correct');
    }
    
    // Show explanation
    questionContainer.classList.add('answered');
    const explanation = questionContainer.querySelector('.practice-explanation');
    if (explanation) {
      explanation.classList.add('show');
    }
  });

  /* ==========================================================================
     PRINT / PDF EXPORT TRIGGER
     ========================================================================== */

  printBtn.addEventListener('click', () => {
    // If not in PDF mode, toggle it temporarily to give browser layout a clean layout,
    // then trigger browser print.
    const initiallySlideshow = !isPdfMode;
    
    if (initiallySlideshow) {
      toggleMode();
    }

    // Small delay to ensure CSS re-render has completed before dialog launches
    setTimeout(() => {
      window.print();
      
      // Revert back if we forced it
      if (initiallySlideshow) {
        toggleMode();
      }
    }, 250);
  });
});
