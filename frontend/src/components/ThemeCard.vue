<template>
  <div class="theme-card">
    <img :src="theme.image_url" alt="quiz image" class="quiz-image" />
    <h3>{{ theme.name }}</h3>
  </div>
</template>

<script>
export default {
  props: {
    theme: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.theme-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.theme-image {
  width: 50px;
  height: 50px;
  margin-bottom: 10px;
}

.theme-card h3 {
  font-size: 16px;
  color: #333;
}
</style>
