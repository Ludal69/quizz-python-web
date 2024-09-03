<template>
  <div class="quiz-question">
    <h2>{{ currentIndex }} / {{ totalQuestions }}</h2>
    <p>{{ question.content }}</p>
    <div class="answers">
      <button
        v-for="answer in question.reponses"
        :key="answer.id"
        @click="selectAnswer(answer.id)"
        :class="{
          correct: selectedAnswer === answer.id && isCorrect(answer.id),
          incorrect: selectedAnswer === answer.id && !isCorrect(answer.id),
        }"
        :disabled="validated"
      >
        {{ answer.content }}
      </button>
    </div>
    <button v-if="validated" @click="next" class="next-button">
      {{ isLastQuestion ? "Voir mon score" : "Question suivante" }}
    </button>
  </div>
</template>

<script>
export default {
  props: {
    question: Object,
    currentIndex: Number,
    totalQuestions: Number,
  },
  data() {
    return {
      selectedAnswer: null,
      validated: false,
    };
  },
  computed: {
    isLastQuestion() {
      return this.currentIndex === this.totalQuestions;
    },
  },
  methods: {
    selectAnswer(answerId) {
      this.selectedAnswer = answerId;
      this.validated = true;
    },
    isCorrect(answerId) {
      return answerId === this.question.correct_answer.id;
    },
    next() {
      this.$emit("next-question");
    },
  },
};
</script>

<style scoped>
.quiz-question {
  background-color: #563d7c;
  padding: 20px;
  border-radius: 10px;
  color: white;
}

.answers button {
  display: block;
  margin: 10px 0;
  padding: 10px;
  background-color: white;
  color: #563d7c;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.answers button.correct {
  background-color: green;
  color: white;
}

.answers button.incorrect {
  background-color: red;
  color: white;
}

.next-button {
  background-color: #ff5678;
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  font-size: 18px;
}

.next-button:hover {
  background-color: #e44a68;
}
</style>
