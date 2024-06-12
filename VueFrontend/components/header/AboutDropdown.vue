<script setup lang="ts">
defineProps<{
  closeMenu?: Function;
}>();

const localePath = useLocalePath();
const { data: translations } = useNuxtData("commonStrings");
const route = useRoute();
const isActive = ref(route.matched[0].path === localePath("/about"));

watch(
  () => route.matched,
  (matched) => {
    isActive.value = matched[0].path === localePath("/about");
  }
);
</script>

<template lang="html">
  <li class="nav-item dropdown">
    <a
      id="about"
      class="nav-link dropdown-toggle link-light"
      href="#"
      role="button"
      data-bs-toggle="dropdown"
      data-bs-auto-close="true"
      aria-expanded="false"
    >
      <span :class="{ 'router-link-active': isActive }">{{ translations.about }}</span>
    </a>
    <ul class="dropdown-menu dropdown-menu-dark border-primary">
      <li>
        <NuxtLink :to="localePath('/about/actors')" class="dropdown-item nav-dropdown" @click="closeMenu">
          {{ translations.collective }}
        </NuxtLink>
      </li>
      <li>
        <NuxtLink :to="localePath('/about/stages')" class="dropdown-item nav-dropdown" @click="closeMenu">
          {{ translations.stages }}
        </NuxtLink>
      </li>
      <li>
        <NuxtLink :to="localePath('/about/history')" class="dropdown-item nav-dropdown" @click="closeMenu">
          {{ translations.history }}
        </NuxtLink>
      </li>
      <li>
        <hr class="dropdown-divider border-primary" />
      </li>
      <li>
        <a
          class="dropdown-item nav-dropdown"
          href="https://www.jobs.bg/company/242425"
          target="_blank"
          rel="noopener noreferrer"
        >
          <span class="d-flex align-items-center">
            {{ translations.careers }}
            <Icon class="ms-2" name="bi:arrow-up-right-square" />
          </span>
        </a>
      </li>
    </ul>
  </li>
</template>

<style lang="css" scoped>
.link-primary {
  text-decoration: none;
}
</style>
