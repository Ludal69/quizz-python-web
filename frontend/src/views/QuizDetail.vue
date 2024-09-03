<template>
  <div class="quiz-detail">
    <h1>{{ quiz.title }}</h1>
    <p>{{ quiz.description }}</p>
    <img :src="quiz.image_url" alt="Quiz image" class="quiz-image" />
    <div class="quiz-info">
      <span>{{ quiz.number_of_questions }} Questions</span>
      <span>Niveau {{ quiz.difficulty }}</span>
    </div>
    <button @click="startQuiz" class="start-quiz-button">
      Commencer le Quiz
    </button>

    <div v-if="quizStarted">
      <QuizQuestion
        v-for="(question, index) in quiz.questions"
        :key="index"
        :question="question"
        :current-index="index + 1"
        :total-questions="quiz.questions.length"
        @validate-answer="validateAnswer"
        @next-question="nextQuestion(index)"
      />
    </div>
  </div>
</template>

<script>
import QuizQuestion from "@/components/QuizQuestion.vue";

export default {
  components: {
    QuizQuestion,
  },
  data() {
    return {
      quiz: {},
      quizStarted: false,
    };
  },
  methods: {
    startQuiz() {
      this.quizStarted = true;
    },
    validateAnswer(correct, userAnswer) {
      // Logique de validation de la réponse
      console.log(correct);
      console.log(userAnswer);
    },
    nextQuestion(index) {
      if (index + 1 === this.quiz.questions.length) {
        // Logique pour afficher le score final
      } else {
        // Logique pour passer à la question suivante
      }
    },
  },
  created() {
    fetch(`http://localhost:8000/api/quiz/${this.$route.params.id}`)
      .then((response) => response.json())
      .then((data) => {
        this.quiz = data;
      });
  },
};
</script>

<style scoped>
.quiz-detail {
  text-align: center;
}

.quiz-image {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  margin: 20px 0;
}

.quiz-info {
  margin: 20px 0;
  display: flex;
  justify-content: space-around;
}

.start-quiz-button {
  background-color: #ff5678;
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  font-size: 18px;
}

.start-quiz-button:hover {
  background-color: #e44a68;
}
</style>
