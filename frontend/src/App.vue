<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<template>
  <div class="app-shell">
    <nav class="top-nav">
      <div class="nav-container">
        <div class="brand">
          <div class="logo-icon">QC</div>
          <span class="logo-text"
            >Care<span class="font-light">Queue</span></span
          >
        </div>

        <div class="nav-links">
          <!-- Currently hardcoded user; will be updated to fetch actual user -->
          <span class="user-profile">Administrator</span>
        </div>
      </div>
    </nav>

    <main class="main-content">
      <RouterView />
    </main>

    <footer class="app-footer">
      2026 CareQueue System | Made by Paul Song
    </footer>
  </div>
</template>

<style scoped>
@reference "./main.css";
.app-shell {
  @apply min-h-screen flex flex-col bg-slate-50 font-sans antialiased;
}

.top-nav {
  @apply bg-white border-b border-slate-200 sticky top-0 z-50;
}

.nav-container {
  @apply max-w-5xl mx-auto px-4 h-16 flex justify-between items-center;
}

.brand {
  @apply flex items-center gap-3;
}

.logo-icon {
  @apply w-8 h-8 bg-blue-600 text-white flex items-center justify-center rounded-lg font-black text-xs;
}

.logo-text {
  @apply text-xl font-bold text-slate-800 tracking-tight;
}

.user-profile {
  @apply text-xs font-bold text-slate-400 uppercase tracking-wider;
}

.content-area {
  @apply flex-grow;
}

.app-footer {
  @apply py-8 text-center text-[10px] text-slate-400 uppercase tracking-[0.2em];
}
</style>
