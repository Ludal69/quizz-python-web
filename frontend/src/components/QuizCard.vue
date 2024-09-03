<template>
  <div class="quiz-card" @click="goToQuizDetail">
    <img :src="quiz.image_url" alt="quiz image" class="quiz-image" />
    <div class="quiz-details">
      <h4>{{ quiz.title }}</h4>
      <div class="quiz-meta">
        <div class="difficulty">
          <font-awesome-icon icon="star" />
          <span>{{ quiz.difficulty }}</span>
        </div>
        <div class="category">
          <font-awesome-icon icon="bookmark" />
          <span>{{ quiz.category }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    quiz: {
      type: Object,
      required: true,
    },
  },
  methods: {
    goToQuizDetail() {
      // Rediriger vers la page de détails du quiz avec l'identifiant du quiz
      this.$router.push({ name: "QuizDetail", params: { id: this.quiz.id } });
    },
  },
};
</script>

<style scoped>
.quiz-card {
  display: flex;
  align-items: center;
  background-color: #ffffff;
  border-radius: 15px;
  padding: 20px;
  margin: 10px 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: left;
  cursor: pointer; /* Ajout d'un curseur pour indiquer que c'est cliquable */
}

.quiz-image {
  width: 100px;
  height: 100px;
  border-radius: 10px;
  margin-right: 20px;
}

.quiz-details {
  flex-grow: 1;
}

.quiz-details h4 {
  margin: 0 0 10px 0;
  font-size: 18px;
  color: #2c3e50;
}

.quiz-meta {
  display: flex;
  align-items: center;
  gap: 20px;
}

.quiz-meta .difficulty,
.quiz-meta .category {
  display: flex;
  align-items: center;
  font-size: 14px;
  color: #7f8c8d;
}
</style>
