<script setup lang="ts">
const { data: translations } = useNuxtData("eventStrings");
const { data: playData } = useNuxtData("playData");
const entaseData = playData.value.entase_data;
</script>

<template lang="html">
  <div class="container pt-4">
    <div class="row text-center fs-5">
      <span v-if="entaseData?.[0]" class="col-12 d-block d-md-none mb-2 date-start">
        <i class="bi bi-calendar3 me-1"></i>
        {{ entaseData?.[0].dateStart }}
      </span>
      <span class="col-6 col-md-4">
        <i class="bi bi-pin-map me-1"></i>
        {{ playData.stage }}
      </span>
      <span v-if="entaseData?.[0]" class="col-4 d-none d-md-block date-start">
        <i class="bi bi-calendar3 me-1"></i>
        {{ entaseData?.[0].dateStart }}
      </span>
      <span v-else class="col-4">{{ translations.soon }}</span>
      <span class="col-6 col-md-4">
        <i class="bi bi-clock-history me-1"></i>
        {{ playData.length }} {{ translations.min }}
      </span>
      <span v-if="entaseData?.[0]" class="col-12 mt-2 mb-1">
        <i class="bi bi-exclamation-circle me-1"></i>
        {{ translations.seats }}
        {{ entaseData?.[0].stats.capacity - entaseData?.[0].stats.selled - entaseData?.[0].stats.reserved }}
      </span>
    </div>
    <hr />
  </div>
</template>

<style lang="css" scoped>
.date-start {
  text-transform: capitalize;
}
</style>
