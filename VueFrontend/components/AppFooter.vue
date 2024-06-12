<script setup lang="ts">
const { data: translations } = useNuxtData("commonStrings");
</script>

<template lang="html">
  <div id="footer" class="mt-auto text-bg-light">
    <footer class="bd-footer py-4 py-md-2">
      <div class="container">
        <div class="row text-center">
          <FooterSocialCol>
            <template #heading>{{ translations.online }}</template>
          </FooterSocialCol>
          <FooterLogoCol />
          <FooterLegalCol :privacy="translations.privacy" :gdpr="translations.gdpr" :public="translations.public">
            <template #heading>{{ translations.legal }}</template>
          </FooterLegalCol>
        </div>
        <p class="text-center text-muted mb-0">&#169; 2023 {{ translations.dkts }}</p>
        <!-- <p class="text-center text-muted">
          Made with <i class="bi bi-heart-fill"></i> by Grand Ant.
        </p> -->
      </div>
    </footer>
  </div>
</template>

<style lang="css" scoped></style>
