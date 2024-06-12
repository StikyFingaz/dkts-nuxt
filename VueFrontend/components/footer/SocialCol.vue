<script setup lang="ts">
// TODO: Make social media links updated per device type
</script>

<template lang="html">
  <div class="col-md-4 mb-3 mb-md-0">
    <h3><slot name="heading"></slot></h3>
    <a href="https://www.facebook.com/theatershumen" class="link-dark" target="_blank" rel="noopener noreferrer">
      <Icon name="bi:facebook" class="footerIcon" />
    </a>
    <a href="https://www.instagram.com/theatreshumen/" class="link-dark" target="_blank" rel="noopener noreferrer">
      <Icon name="bi:instagram" class="footerIcon" />
    </a>
    <a
      href="https://www.youtube.com/channel/UCH_Y_6oQvor2qyFkmBtAoXw?cbrd=1"
      class="link-dark"
      target="_blank"
      rel="noopener noreferrer"
    >
      <Icon name="bi:youtube" class="footerIcon" />
    </a>
    <a
      href="https://open.spotify.com/show/1o2riigiuhcISFq9rp1ajo"
      class="link-dark"
      target="_blank"
      rel="noopener noreferrer"
    >
      <Icon name="bi:spotify" class="footerIcon" />
    </a>
    <a href="https://podcast.dktshumen.com" class="link-dark" target="_blank" rel="noopener noreferrer">
      <Icon name="bi:rss" class="footerIcon" />
    </a>
    <div class="span">
      <a href="mailto:info@dktshumen.com" class="link-dark" rel="noopener noreferrer">
        <Icon name="bi:envelope" class="footerIcon fs-6" />info@dktshumen.com
      </a>
    </div>
    <div class="span">
      <a href="mailto:theatreshumen@gmail.com" class="link-dark" rel="noopener noreferrer">
        <Icon name="bi:envelope" class="footerIcon fs-6" />theatreshumen@gmail.com
      </a>
    </div>
    <div class="span">
      <a href="tel:+359896140044" class="link-dark" rel="noopener noreferrer">
        <Icon name="bi:telephone-outbound" class="footerIcon fs-6" />+359 896 140 044
      </a>
    </div>
  </div>
</template>

<style lang="css" scoped>
.footerIcon {
  font-size: xx-large;
  margin: 5px;
}
</style>
