export interface Patient {
  id?: number;
  name: string;
  symptoms: string;
  priority: "Critical" | "Moderate" | "Routine";
  check_in_time?: string;
}

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const patientService = {
  // Sorted by priority
  async getPatients(): Promise<Patient[]> {
    const response = await fetch(`${API_BASE_URL}/patients`);
    if (!response.ok) throw new Error("Failed to fetch patients");
    return response.json();
  },

  // Add a new patient
  async checkInPatient(patient: Patient): Promise<Patient> {
    const response = await fetch(`${API_BASE_URL}/patients`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(patient),
    });
    if (!response.ok) throw new Error("Check-in failed");
    return response.json();
  },

  async resolvePatient(id: number): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/patients/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error(
        "Failed to resolve patient. Please ensure the server is running and try again.",
      );
    }
  },
};
