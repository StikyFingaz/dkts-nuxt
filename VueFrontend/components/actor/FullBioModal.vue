<script setup lang="ts">
defineProps<{
  close?: string;
}>();

const route = useRoute();
const { data: actor } = useNuxtData(route.params.nickname);
</script>

<template lang="html">
  <div class="modal fade modal-lg" id="fullTextModal" tabindex="-1" aria-labelledby="Full bio popup" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title display-5">
            {{ getTranslation(actor, "name") }}
          </h1>
        </div>
        <div class="modal-body text-start ms-1 me-1 ms-md-4 me-md-4">
          <span ref="playDescription" id="playDescription">
            <p v-for="p in getTranslation(actor, 'short_bio').split('\n')" class="lead">{{ p }}</p>
          </span>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ close }}</button>
        </div>
      </div>
    </div>
  </div>
</template>
