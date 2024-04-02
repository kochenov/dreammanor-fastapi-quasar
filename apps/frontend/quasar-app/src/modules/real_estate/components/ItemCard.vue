<template>
  <q-card class="my-card" flat bordered>
    <div class="position-relative">
      <q-img
        :ratio="16 / 9"
        :src="item.link_img || '/img/not-image-house.jpg'"
      />
      <q-icon
        v-if="item.is_video"
        class="position-absolute"
        name="camera_outdoor"
        size="25px"
        color="orange-6"
      />
    </div>

    <q-card-section>
      <q-fab
        color="primary"
        icon="keyboard_arrow_up"
        direction="up"
        class="absolute"
        padding="10px"
        style="top: 0; right: 12px; transform: translateY(-50%)"
      >
        <template v-slot:icon="{ opened }">
          <q-icon
            :class="{ 'example-fab-animate--hover': opened !== true }"
            name="keyboard_arrow_up"
          />
        </template>

        <template v-slot:active-icon="{ opened }">
          <q-icon
            :class="{ 'example-fab-animate': opened === true }"
            name="close"
          />
        </template>
        <q-fab-action
          label="Не подходит"
          label-position="left"
          external-label
          @click="$emit('editItem', { id: item.id, status_id: 4 })"
          color="negative"
          icon="delete_sweep"
        />
        <q-fab-action
          label="Комментировать"
          @click="$emit('addComment', item)"
          label-position="left"
          external-label
          color="warning"
          icon="edit_note"
        />
        <q-fab-action
          label="Опубликовать"
          label-position="left"
          external-label
          color="positive"
          icon="post_add"
        />
      </q-fab>

      <div class="row no-wrap items-center">
        <div class="col text-subtitle1 ellipsis">{{ item.title }}</div>
        <div
          class="col-auto text-grey text-caption q-pt-md row no-wrap items-center"
        >
          <q-icon name="place" />
          250 ft
        </div>
      </div>
    </q-card-section>

    <q-card-section class="q-pt-none">
      <div class="text-subtitle1 text-weight-bolder text-right">
        <q-icon name="currency_ruble" style="color: green; font-size: 1.4em" />
        {{ format_number(item.price) }}
      </div>
      <div class="text-caption text-grey">
        {{ item.comment }}
      </div>
    </q-card-section>

    <q-separator />

    <q-card-actions class="flex justify-between">
      <q-icon name="today" size="25px">
        <q-tooltip anchor="top middle" self="bottom middle" :offset="[10, 10]">
          {{ date_ru(item.created_ad) }}
        </q-tooltip>
      </q-icon>

      <q-btn :href="item.link" target="_blank" flat color="primary">
        Смотреть
      </q-btn>
    </q-card-actions>
  </q-card>
</template>

<script setup>
import { date_ru, format_number } from "src/utils/helpers";
const props = defineProps({
  item: Object,
});
</script>

<style lang="scss" scoped>
.position-absolute {
  bottom: 0;
  left: 0;
  position: absolute;
}
.position-relative {
  position: relative;
}

.example-fab-animate,
.q-fab:hover .example-fab-animate--hover {
  animation: example-fab-animate 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
  perspective: 1000px;
}
@keyframes example-fab-animate {
  10%,
  90% {
    transform: translate3d(-1px, 0, 0);
  }

  20%,
  80% {
    transform: translate3d(2px, 0, 0);
  }
  30%,
  50%,
  70% {
    transform: translate3d(-4px, 0, 0);
  }
  40%,
  60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>
