import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CheckInForm from "../components/CheckInForm.vue";
import PatientCard from "../components/PatientCard.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/check-in",
      name: "check-in",
      component: CheckInForm,
    },
    {
      path: "/patient/:id",
      name: "patient-details",
      component: PatientCard,
    },
  ],
});

export default router;
