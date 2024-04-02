<template>
  <div class="box q-my-lg q-mx-xs">
    <q-card class="my-card" flat bordered>
      <div class="row wrap-md no-wrap-lg items-center title-container">
        <div class="col">
          <!-- Заголовок -->
          <q-item>
            <q-item-section v-if="title_icon" avatar>
              <q-avatar :icon="title_icon" />
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-subtitle2"
                >{{ page_title }}

                <q-badge outline v-if="total" align="middle" color="primary">
                  {{ total || 0 }}
                </q-badge>
              </q-item-label>
              <q-item-label v-if="page_subtitle" caption class="text-red-10">
                {{ page_subtitle }}
              </q-item-label>
            </q-item-section>
          </q-item>
        </div>
        <div class="col-auto">
          <slot name="head_nav_right"> head_nav_right</slot>
        </div>
      </div>
      <q-separator />

      <q-card-section class="card-content" horizontal>
        <q-card-section class="col-lg col-sm-12 col-md-8">
          <slot name="main_content">main_content </slot>
        </q-card-section>

        <q-separator v-if="side_right" vertical />

        <q-card-section
        v-if="side_right"
          class="col-lg-3 col-sm-12 col-md-4 col-xl-2 position-relative"
        >
          <slot name="side_right"> side_right</slot>
        </q-card-section>
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup>
const props = defineProps({
  page_title: { type: String, required: true },
  page_subtitle: String,
  title_icon: String,
  total: { type: Number, default: 0 },
  side_right: { type: Boolean, default: true}
});
</script>

<style lang="scss" scoped>
@media (max-width: $breakpoint-sm-max) {
  .title-container {
    flex-direction: column;
    padding: 20px 0;
  }
  @media (max-width: $breakpoint-sm-max) {
  .card-content {
    flex-direction: column-reverse;
  }
}
}
</style>
