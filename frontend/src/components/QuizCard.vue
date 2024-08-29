<template>
  <div class="quiz-card">
    <img :src="themeImage" alt="quiz image" class="quiz-image" />
    <div class="quiz-details">
      <h4>{{ quiz.title }}</h4>
      <div class="quiz-meta">
        <div class="difficulty">
          <!-- <img src="@/assets/icons/difficulty-icon.svg" alt="Difficulty icon" /> -->
          <span>{{ quiz.difficulty }}</span>
        </div>
        <div class="category">
          <!-- <img src="@/assets/icons/category-icon.svg" alt="Category icon" /> -->
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
  computed: {
    themeImage() {
      // Si le thème est "Céline Dion", on utilise l'image spécifique
      // if (this.theme.name === "Céline Dion") {
      //   return require("@/assets/images/icons/celine.png");
      // } else {
      //   return this.theme.image; // Sinon on utilise l'image par défaut du thème
      // }

      return require("@/assets/images/icons/celine.png");
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

.quiz-meta img {
  width: 16px;
  height: 16px;
  margin-right: 5px;
}
</style>
