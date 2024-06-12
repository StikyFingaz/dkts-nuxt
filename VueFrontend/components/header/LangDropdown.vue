<script setup lang="ts">
const props = defineProps<{
  closeMenu?: Function;
}>();

const switchLocalePath = useSwitchLocalePath();
</script>

<template lang="html">
  <li class="nav-item dropdown">
    <a
      id="languageDropdown"
      class="nav-link dropdown-toggle link-light"
      href="#"
      role="button"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      <Icon class="mb-1" name="bi:globe2" />
    </a>
    <ul class="dropdown-menu dropdown-menu-dark border-primary">
      <li>
        <NuxtLink :to="switchLocalePath('bg')" class="dropdown-item nav-dropdown lang-btn" @click="closeMenu()">
          <div class="d-flex align-items-center">
            <Icon class="me-2" name="flag:bg-4x3" />
            Български
          </div>
        </NuxtLink>
      </li>
      <li>
        <NuxtLink :to="switchLocalePath('en')" class="dropdown-item nav-dropdown lang-btn" @click="closeMenu()">
          <span class="d-flex align-items-center">
            <Icon class="me-2" name="flag:gb-4x3" />
            English
          </span>
        </NuxtLink>
      </li>
    </ul>
  </li>
</template>

<style lang="css" scoped></style>
