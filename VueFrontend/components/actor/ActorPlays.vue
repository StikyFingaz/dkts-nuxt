<script setup lang="ts">
const route = useRoute();
const { data: translations } = useNuxtData("aboutStrings");
const { data: actor } = useNuxtData(route.params.nickname);
const displaySize = useState("displaySize");
</script>

<template lang="html">
  <div v-if="actor && actor.plays.length > 0" class="container-fluid text-bg-dark mt-3 mt-lg-0 mb-3">
    <h3 class="container pt-2">
      {{ translations.watch }} {{ getTranslation(actor, "name") }} {{ translations.watchIn }}:
    </h3>
    <div :class="{ container: ['md', 'lg', 'xl', 'xxl'].includes(displaySize) }">
      <div id="playsCarousel" class="container-fluid">
        <Swiper
          :modules="[SwiperAutoplay]"
          slidesPerView="auto"
          :centeredSlidesBounds="true"
          :centerInsufficientSlides="true"
          :autoplay="{
            delay: 3500,
            disableOnInteraction: true,
          }"
        >
          <SwiperSlide v-for="play in actor.plays" :key="play.slug" class="m-2">
            <!-- <div v-for="play in plays" class="col-11 col-md-6 col-lg-4 col-xl-3 card-col p-2"> -->
            <PlayCard :playLink="play.slug" :isCurrent="play.current" :ticket-link="play.entase_data?.[0]?.id ?? null">
              <template #images>
                <!-- <img
                  v-if="['xs', 'sm', 'md'].includes(displaySize)"
                  :src="setThumborUrl(`/media/plays/${play.slug}/poster.jpg`, 'unsafe/340x0/filters:format(webp)')"
                  alt=""
                  class="card-img-top img-fluid d-block d-lg-none pic-sm"
                  width="340"
                  height="476"
                  loading="lazy"
                />
                <img
                  v-if="['lg', 'xl', 'xxl'].includes(displaySize)"
                  :src="setThumborUrl(`/media/plays/${play.slug}/poster.jpg`, 'unsafe/310x0/filters:format(webp)')"
                  class="card-img-top img-fluid d-none d-lg-block pic-lg"
                  alt=""
                  width="310"
                  height="434"
                /> -->
                <NuxtImg
                  format="webp"
                  :src="`/media/plays/${play.slug}/poster.jpg`"
                  alt=""
                  class="card-img-top img-fluid gallery-slide"
                  width="960"
                  height="1344"
                  sizes="310px md:40vw lg:300px"
                  loading="lazy"
                />
              </template>
              <template #name>
                {{ getTranslation(play, "name") }}
              </template>
            </PlayCard>
          </SwiperSlide>
        </Swiper>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped>
.swiper-slide {
  max-width: 310px;

  @media (min-width: 768px) {
    max-width: 40vw;
  }

  @media (min-width: 992px) {
    max-width: 300px;
  }
}
</style>
