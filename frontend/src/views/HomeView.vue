<script setup lang="ts">
import { ref, onMounted } from "vue";
import { patientService, type Patient } from "../api/patientService";
import PatientCard from "../components/PatientCard.vue";
import CheckInForm from "../components/CheckInForm.vue";

const patients = ref<Patient[]>([]);
const isLoading = ref(true);
const error = ref<string | null>(null);

const refreshQueue = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    patients.value = await patientService.getPatients();
  } catch (err) {
    error.value =
      "Unable to connect to the server. Please check your connection and try again.";
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

onMounted(refreshQueue);
</script>

<template>
  <div class="dashboard-wrapper">
    <div class="container">
      <header class="main-header">
        <div class="logo-group">
          <h1 class="brand-name">CareQueue</h1>
          <span class="status-indicator">Live Queue</span>
        </div>
        <button class="refresh-btn" @click="refreshQueue" :disabled="isLoading">
          <span v-if="!isLoading">Refresh Dashboard</span>
          <span v-else>Syncing...</span>
        </button>
      </header>

      <section class="form-section">
        <CheckInForm @patientAdded="refreshQueue" />
      </section>

      <section class="queue-section">
        <div class="section-header">
          <h2 class="section-title">Current Patient Load</h2>
          <span class="count-badge">{{ patients.length }} Waiting</span>
        </div>

        <div v-if="error" class="error-banner">{{ error }}</div>

        <div v-if="isLoading && patients.length === 0" class="loading-state">
          Fetching patient records...
        </div>

        <div v-else-if="patients.length > 0" class="card-grid">
          <PatientCard
            v-for="p in patients"
            :key="p.id"
            :id="p.id!"
            :name="p.name"
            :symptoms="p.symptoms"
            :priority="p.priority"
            :checkInTime="p.check_in_time!"
            @resolved="refreshQueue"
          />
        </div>

        <div v-else class="empty-state">
          <p>No patients currently in the queue.</p>
          <small>Use the form above to check in a new patient.</small>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
@reference "../main.css";
.dashboard-wrapper {
  @apply min-h-screen bg-slate-50 py-10 px-4;
}

.container {
  @apply max-w-4xl mx-auto;
}

.main-header {
  @apply flex justify-between items-end mb-10 border-b border-slate-200 pb-6;
}

.brand-name {
  @apply text-3xl font-black text-blue-900 tracking-tight leading-none;
}

.status-indicator {
  @apply text-xs font-bold text-blue-600 uppercase tracking-widest mt-2 block;
}

.refresh-btn {
  @apply text-xs font-bold text-slate-500 bg-white border border-slate-200 px-4 py-2 rounded-lg hover:bg-slate-100 transition-colors disabled:opacity-50;
}

.section-header {
  @apply flex justify-between items-center mb-6;
}

.section-title {
  @apply text-lg font-bold text-slate-800;
}

.count-badge {
  @apply bg-slate-200 text-slate-600 text-[10px] font-bold px-2 py-0.5 rounded-full;
}

.error-banner {
  @apply bg-red-100 border border-red-200 text-red-700 p-4 rounded-xl text-sm mb-6;
}

.loading-state,
.empty-state {
  @apply text-center py-20 border-2 border-dashed border-slate-200 rounded-3xl text-slate-400;
}

.empty-state p {
  @apply font-bold text-slate-600;
}

.card-grid {
  @apply space-y-2;
}
</style>
