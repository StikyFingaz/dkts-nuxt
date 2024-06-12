<script setup lang="ts">
const { data: translations } = useNuxtData("commonStrings");
</script>

<template lang="html">
  <div class="col-md-4">
    <div class="text-align">
      <h3><slot name="heading"></slot></h3>
      <!-- TODO: Make the links show actual Information -->
      <ul class="list-unstyled">
        <li>
          <a class="link-dark" href="/policies/privacy-policy.pdf" rel="noreferrer" target="_blank">
            {{ translations.privacy }}
          </a>
        </li>
        <li>
          <a class="link-dark" href="/policies/gdpr-policy.pdf" rel="noreferrer" target="_blank">
            {{ translations.gdpr }}
          </a>
        </li>
        <li>
          <a class="link-dark" href="/policies/public-info.pdf" rel="noreferrer" target="_blank">
            {{ translations.public }}
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style lang="css" scoped>
.text-align {
  width: fit-content;
  text-align: left;
  margin: auto;
}
</style>
