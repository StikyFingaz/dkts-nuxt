<!-- Custom nav-toggler from Mikael Ainalem -->
<!-- https://codepen.io/ainalem/pen/bGmzRbE -->
<script setup lang="ts">
const props = defineProps<{
  togglerState?: bool;
}>();

let menu, animate1, animate2, animate3;

const values1 = [
  "M 84,24 C 84,24 61.333333,24.001 50,24.001 38.666667,24.001 16,24 16,24",
  "M 82,24 C 82,24 66.957389,30.5 50,30.5 33.042611,30.5 18,24 18,24",
  "M 80,24 C 80,24 61.663104,37 50,37 38.336896,37 20,24 20,24",
  "M 78,24 C 78,24 55.685686,43.5 50,43.5 44.314314,43.5 22,24 22,24",
  "M 76,24 C 76,24 50.055365,50 50,50 49.94463,50 24,24 24,24",
];
const values2 = [
  "M 84,50 H 50 16",
  "M 75.5,50 H 50 24.5",
  "M 67,50 H 50 33",
  "M 58.5,50 H 50 41.5",
  "M 50.001,50 H 50 49.99",
];
const values3 = [
  "M 84,76 C 84,76 61.333333,76.001 50,76.001 38.666667,76.001 16,76 16,76",
  "M 82,76 C 82,76 66.957389,69.5 50,69.5 33.042611,69.5 18,76 18,76",
  "M 80,76 C 80,76 61.663104,63 50,63 38.336896,63 20,76 20,76",
  "M 78,76 C 78,76 55.685686,56.5 50,56.5 44.314314,56.5 22,76 22,76",
  "M 76,76 C 76,76 50.055365,50 50,50 49.944635,50 24,76 24,76",
];

function toggleAnimation(values, animate) {
  animate.setAttribute("values", !props.togglerState ? values.join("; ") : values.slice().reverse().join("; "));
  animate.beginElement();
}

function handleClick() {
  toggleAnimation(values1, animate1);
  toggleAnimation(values2, animate2);
  toggleAnimation(values3, animate3);

  menu.setAttribute("aria-expanded", !props.togglerState);
  menu.setAttribute("aria-label", !props.togglerState ? "Close Menu" : "Open Menu");
}

function initPath(clazz, descriptor) {
  const path = document.querySelector(clazz);
  path.setAttribute("d", descriptor);
}

onMounted(() => {
  menu = document.querySelector(".menu");
  animate1 = document.querySelector(".animate1");
  animate2 = document.querySelector(".animate2");
  animate3 = document.querySelector(".animate3");

  initPath(".path1", values1[0]);
  initPath(".path2", values2[0]);
  initPath(".path3", values3[0]);

  watchEffect(() => {
    handleClick();
  });
});
</script>

<template lang="html">
  <button
    id="togglerButton"
    class="menu navbar-toggler"
    type="button"
    @click="handleClick()"
    data-bs-toggle="offcanvas"
    data-bs-target="#offcanvasNavbar"
    aria-controls="offcanvasNavbar"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <svg width="32" height="32" viewBox="0 0 100 100" class="icon">
      <path class="path1">
        <animate class="animate1" attributeName="d" dur="0.35s" repeatCount="1" fill="freeze" />
      </path>
      <path class="path2">
        <animate class="animate2" attributeName="d" dur="0.35s" repeatCount="1" fill="freeze" />
      </path>
      <path class="path3">
        <animate class="animate3" attributeName="d" dur="0.35s" repeatCount="1" fill="freeze" />
      </path>
    </svg>
  </button>
</template>

<style lang="css" scoped>
.icon {
  fill: none;
  margin-top: 0px;
  stroke: white;
  stroke-width: 12;
  stroke-linecap: square;
  stroke-linejoin: round;
}
</style>
