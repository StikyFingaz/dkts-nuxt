<script setup lang="ts">
const { data: translations } = useNuxtData("eventStrings");
const { data: play } = useNuxtData("playData");
</script>

<template lang="html">
  <div class="container text-center fs-5 pb-3">
    <Swiper
      :modules="[SwiperAutoplay, SwiperPagination, SwiperVirtual]"
      slidesPerView="1"
      :autoplay="{
        delay: 3500,
        disableOnInteraction: true,
      }"
    >
      <SwiperSlide v-if="play.author">
        <span class="p-2">{{ translations.author }}: {{ getTranslation(play, "author") }}</span>
      </SwiperSlide>
      <SwiperSlide v-if="play.director">
        <span class="p-2">{{ translations.director }}: {{ getTranslation(play, "director") }}</span>
      </SwiperSlide>
      <SwiperSlide v-if="play.scenographer">
        <span class="p-2">{{ translations.scenographer }}: {{ getTranslation(play, "scenographer") }}</span>
      </SwiperSlide>
      <SwiperSlide v-if="play.composer">
        <span class="p-2">{{ translations.composer }}: {{ getTranslation(play, "composer") }}</span>
      </SwiperSlide>
      <SwiperSlide v-if="play.dramatization">
        <span class="p-2">{{ translations.dramatization }}: {{ getTranslation(play, "dramatization") }}</span>
      </SwiperSlide>
      <SwiperSlide v-if="play.artistic_director">
        <span class="p-2">{{ translations.artistic }}: {{ getTranslation(play, "artistic_director") }}</span>
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style lang="css" scoped></style>
