<template>
  <div id="app">
    <h1>{{ message }} oops6789101112</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Loading...",
    };
  },
  created() {
    fetch("http://localhost:8000/api/hello/")
      .then((response) => response.json())
      .then((data) => {
        this.message = data.message;
      })
      .catch((error) => {
        (this.message = "Failed to fetch message4: "), error.message;
      });
  },
};
</script>
