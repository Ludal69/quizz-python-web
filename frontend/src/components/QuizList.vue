<template>
  <div class="quiz-list">
    <input
      type="text"
      v-model="search"
      placeholder="Rechercher un quiz..."
      class="search-bar"
    />
    <select v-model="difficulty" class="filter-select">
      <option value="">Tous les niveaux</option>
      <option value="easy">Facile</option>
      <option value="medium">Moyen</option>
      <option value="hard">Difficile</option>
    </select>
    <div class="quiz-cards">
      <QuizCard v-for="quiz in filteredQuizzes" :key="quiz.id" :quiz="quiz" />
    </div>
  </div>
</template>

<script>
import QuizCard from "@/components/QuizCard.vue";

export default {
  components: {
    QuizCard,
  },
  props: {
    quizzes: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      search: "",
      difficulty: "",
    };
  },
  computed: {
    filteredQuizzes() {
      return this.quizzes.filter((quiz) => {
        return (
          quiz.title.toLowerCase().includes(this.search.toLowerCase()) &&
          (this.difficulty === "" || quiz.difficulty === this.difficulty)
        );
      });
    },
  },
};
</script>

<style scoped>
.quiz-list {
  padding: 20px;
}

.search-bar,
.filter-select {
  width: calc(100% - 40px);
  max-width: 400px;
  padding: 10px;
  margin: 10px auto;
  display: block;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.quiz-cards {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
