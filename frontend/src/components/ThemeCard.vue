<template>
  <div class="theme-card">
    <img :src="themeImage" alt="theme.name" class="theme-image" />
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
