<script setup lang="ts">
import { ref } from "vue";
import { patientService } from "../api/patientService";

const emit = defineEmits(["patientAdded"]);

// Form State
const name = ref("");
const symptoms = ref("");
const priority = ref<"Critical" | "Moderate" | "Routine">("Routine");
const isSubmitting = ref(false);

const handleSubmit = async () => {
  if (!name.value || !symptoms.value) return;

  isSubmitting.value = true;
  try {
    await patientService.checkInPatient({
      name: name.value,
      symptoms: symptoms.value,
      priority: priority.value,
    });

    name.value = "";
    symptoms.value = "";
    priority.value = "Routine";

    emit("patientAdded");
  } catch (err) {
    alert(
      "Check-in failed. Please ensure the server is running and try again.",
    );
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <section class="form-container">
    <form @submit.prevent="handleSubmit" class="check-in-form">
      <h2 class="form-title">New Patient Admission</h2>

      <div class="input-group">
        <label for="name">Patient Full Name</label>
        <input id="name" v-model="name" type="text" required />
      </div>

      <div class="input-group">
        <label for="symptoms">Primary Symptoms / Reason for Visit</label>
        <textarea id="symptoms" v-model="symptoms" required></textarea>
      </div>

      <div class="form-footer">
        <div class="priority-selector">
          <label>Triage Priority</label>
          <select v-model="priority">
            <option value="Routine">Routine</option>
            <option value="Moderate">Moderate</option>
            <option value="Critical">Critical</option>
          </select>
        </div>

        <button type="submit" :disabled="isSubmitting" class="submit-btn">
          <span v-if="!isSubmitting">Complete Check-In</span>
          <span v-else class="loader"> Processing...</span>
        </button>
      </div>
    </form>
  </section>
</template>

<style scoped>
@reference "../main.css";
.form-container {
  @apply mb-12;
}

.check-in-form {
  @apply bg-white p-8 rounded-2xl shadow-sm border border-slate-200;
}

.form-title {
  @apply text-xl font-bold text-slate-800 mb-6 flex items-center gap-2;
}

.input-group {
  @apply mb-5;
}

.input-group label {
  @apply block text-xs font-bold text-slate-400 uppercase tracking-wider mb-2;
}

.input-group input,
.input-group textarea {
  @apply w-full p-3 bg-slate-50 border border-slate-200 rounded-xl outline-none transition-all focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500;
}

.input-group text-area {
  @apply h-24 resize-none;
}

.form-footer {
  @apply flex flex-col md:flex-row justify-between items-end gap-6 mt-8 pt-6 border-t border-slate-100;
}

.priority-selector {
  @apply w-full md:w-auto;
}

.priority-selector label {
  @apply block text-[10px] font-black text-slate-400 uppercase mb-2;
}

.priority-selector select {
  @apply w-full md:w-48 p-2.5 bg-slate-100 border-none rounded-lg text-sm font-bold text-slate-700 outline-none;
}

.submit-btn {
  @apply w-full md:w-auto bg-blue-600 text-white px-8 py-3 rounded-xl font-bold shadow-lg
    shadow-blue-200 hover:bg-blue-700 hover:shadow-blue-300 transition-all active:scale-95 disabled:bg-slate-300 disabled:shadow-none;
}

.loader {
  @apply animate-pulse;
}
</style>
