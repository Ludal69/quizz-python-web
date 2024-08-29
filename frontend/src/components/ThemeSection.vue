<template>
  <div class="theme-section">
    <h2>Thématiques</h2>
    <div class="themes-grid">
      <ThemeCard v-for="theme in themes" :key="theme.id" :theme="theme" />
    </div>
  </div>
</template>

<script>
import ThemeCard from "@/components/ThemeCard.vue";

export default {
  components: {
    ThemeCard,
  },
  props: {
    themes: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.theme-section {
  padding: 20px;
}

.themes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 20px;
}
</style>
