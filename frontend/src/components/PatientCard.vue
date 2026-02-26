<script setup lang="ts">
import { computed } from "vue";
import { patientService } from "../api/patientService";

const props = defineProps<{
  id: number;
  name: string;
  symptoms: string;
  priority: "Critical" | "Moderate" | "Routine";
  checkInTime: string;
}>();

const emit = defineEmits(["resolved"]);

const handleResolve = async () => {
  if (confirm(`Mark ${props.name} as resolved?`)) {
    try {
      await patientService.resolvePatient(props.id);
      emit("resolved");
    } catch (err) {
      console.error(err);
    }
  }
};

// Format timestamp to relative time
const formattedTime = computed(() => {
  return new Date(props.checkInTime).toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  });
});

// Map priority to color
const priorityColor = computed(() => {
  switch (props.priority) {
    case "Critical":
      return "var(--color-urgency-red)";
    case "Moderate":
      return "#f59e0b";
    default:
      return "#94a3b8";
  }
});
</script>

<template>
  <div class="patient-card" :class="priority.toLowerCase()">
    <div class="info-section">
      <h3 class="patient-name">{{ name }}</h3>
      <p class="symptoms-text">{{ symptoms }}</p>
    </div>

    <div class="status-section">
      <span class="priority-badge">{{ priority }}</span>
      <time class="timestamp">Checked in: {{ formattedTime }}</time>
    </div>

    <div class="action-section">
      <button class="resolve-btn" @click="handleResolve">
        <span class="btn-icon">✅</span>
        Resolve Case
      </button>
    </div>
  </div>
</template>

<style scoped>
@reference "../main.css";
.patient-card {
  @apply flex justify-between items-center p-5 mb-4 rounded-xl border-l-8 bg-white shadow-sm transition-all;
  border-left-color: v-bind(priorityColor);
}

.patient-card:hover {
  @apply shadow-md transform translate-x-1;
}

.patient-card.critical {
  @apply bg-red-50/50;
}

.patient-name {
  @apply text-lg font-bold text-slate-900 leading-tight;
}

.symptoms-text {
  @apply text-sm text-slate-500 italic;
}

.status-section {
  @apply text-right flex flex-col items-end;
}

.priority-badge {
  @apply text-[10px] font-black uppercase tracking-widest px-2 py-1 rounded-md mb-2;
  background-color: v-bind(priorityColor);
}

.timestamp {
  @apply text-xs font-medium text-slate-400;
}

.resolve-btn {
  @apply flex items-center gap-2 bg-slate-100 text-slate-700 px-5 py-2.5 rounded-xl font-bold
    text-sm transition-all border border-transparent hover:bg-blue-600 hover:text-white hover:shadow-lg hover:shadow-blue-100;
}

.btn-icon {
  @apply text-lg leading-none;
}
</style>
