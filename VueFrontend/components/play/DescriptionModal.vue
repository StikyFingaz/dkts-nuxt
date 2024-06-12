<script setup lang="ts">
defineProps<{
  playName: string;
  fullDescription: string;
  close: str;
}>();
</script>

<template lang="html">
  <div
    class="modal fade modal-lg"
    id="fullDescriptionModal"
    tabindex="-1"
    aria-labelledby="Full description popup"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title display-6">
            {{ playName }}
          </h1>
        </div>
        <div class="modal-body text-start ms-1 me-1 ms-md-4 me-md-4">
          <span ref="playDescription" id="playDescription">
            <p v-for="p in fullDescription.split('\n')" class="lead">{{ p }}</p>
          </span>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ close }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped></style>
