<template>
  <div>
    <ThemeSection :themes="themes" />
    <QuizList :quizzes="quizzes" />
  </div>
</template>

<script>
import ThemeSection from "@/components/ThemeSection.vue";
import QuizList from "@/components/QuizList.vue";

export default {
  components: {
    ThemeSection,
    QuizList,
  },
  data() {
    return {
      themes: [], // Liste des thèmes, à remplir via une requête API
      quizzes: [], // Liste des quizzes, à remplir via une requête API
    };
  },
  created() {
    // Exemple de fetch pour les thèmes
    fetch("http://localhost:8000/api/themes/")
      .then((response) => response.json())
      .then((data) => {
        this.themes = data;
      });

    // Exemple de fetch pour les quizzes
    fetch("http://localhost:8000/api/quizzes/")
      .then((response) => response.json())
      .then((data) => {
        this.quizzes = data;
      });
  },
};
</script>
