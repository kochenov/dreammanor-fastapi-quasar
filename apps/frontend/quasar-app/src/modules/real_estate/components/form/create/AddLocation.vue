<template>
  <!-- Адрес -->
  <div class="row q-mt-sm wrap q-col-gutter-md">
    <q-select
      :key="modal_form_add_region"
      class="col-12 col-sm"
      v-model="region"
      filled
      use-input
      input-debounce="0"
      label="Выбрать регион"
      :options="region_id_options"
      @update:modelValue="loadDistrict()"
      @filter="region_id_filter_fn"
      behavior="dialog"
      :loading="load_regions_status"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список регионов пуст. Добавьте новый регион
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_region = true"
        />
      </template>
      <q-dialog
        v-model="modal_form_add_region"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить новый регион</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_region"
              label="Введите название региона"
              dense
              error-message="Такой регион уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn flat label="ДОБАВИТЬ" @click="save_new_region_to_base" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>

    <q-select
      :key="modal_form_add_district"
      class="col-12 col-sm"
      v-model="district"
      filled
      :disable="!region && load_regions_status"
      :error="!region"
      error-message="Выбирите сначала регион"
      use-input
      input-debounce="0"
      label="Выбрать район"
      :options="district_id_options"
      @update:modelValue="loadSettlementTypes()"
      @filter="district_id_filter_fn"
      behavior="dialog"
      :loading="load_districts_status"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список районов пуст. Добавьте новый район
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_district = true"
        />
      </template>
      <q-dialog
        v-if="region"
        v-model="modal_form_add_district"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить новый район</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_district"
              label="Введите название региона"
              dense
              error-message="Такой регион уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn flat label="ДОБАВИТЬ" @click="save_new_district_to_base" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>

    <q-select
      :key="modal_form_add_settlement_type"
      class="col-12 col-sm"
      v-model="settlement_type"
      filled
      use-input
      input-debounce="0"
      label="Выбрать тип поселения"
      :options="settlement_type_id_options"
      @update:modelValue="loadSettlements"
      @filter="settlement_type_id_filter_fn"
      behavior="dialog"
      :loading="load_settlement_types_status"
      :disable="!region || !district"
      :error="!region || !district"
      error-message="Выберите сначала регион и район"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список типов поселений пуст. Добавьте новый тип
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_settlement_type = true"
        />
      </template>
      <q-dialog
        v-model="modal_form_add_settlement_type"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить тип поселения</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_settlement_type"
              label="Введите название типа поселения"
              dense
              error-message="Такой тип уже есть"
            />
            <q-input
              class="q-pt-md"
              v-model="new_settlement_type_i"
              label="Как будет на вопрос где?"
              dense
              error-message="Такой тип уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn
              flat
              label="ДОБАВИТЬ"
              @click="save_new_settlement_type_to_base"
            />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>

    <q-select
      @blur="updateFullAdress"
      :key="modal_form_add_settlement"
      class="col-12 col-sm"
      v-model="settlement"
      filled
      :disable="!region || !district || !settlement_type"
      :error="!region || !district || !settlement_type"
      error-message="Выбирите сначала регион, район и тип поселения"
      use-input
      input-debounce="0"
      label="Выбрать поселение"
      :options="settlement_id_options"
      @focus="loadSettlements()"
      @filter="settlement_id_filter_fn"
      behavior="dialog"
      :loading="load_settlements_status"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список поселений пуст. Добавьте новое поселение
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_settlement = true"
        />
      </template>
      <q-dialog
        v-if="region && district"
        v-model="modal_form_add_settlement"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить поселение</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_settlement"
              label="Введите название поселения"
              dense
              error-message="Такое поселение уже есть"
            />
            <q-input
              class="q-pt-md"
              v-model="new_settlement_i"
              label="Как будет на вопрос Где?"
              dense
              error-message="Такое поселение уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn flat label="ДОБАВИТЬ" @click="save_new_settlement_to_base" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>
  </div>

  <q-separator color="orange q-my-lg" inset />

  <!-- Полный адрес -->
  <q-input
    class="q-my-md"
    filled
    autocomplete="Off"
    v-model="full_adress"
    label="Полный адрес *"
    hint="Полный адрес в формате: Регион, район, село, улица, № дома"
    lazy-rules
    :rules="[(val) => (val && val.length > 0) || 'Заполнять обязательно']"
  />

  <q-stepper-navigation>
    <q-btn
      @click="
        full_adress &&
        region &&
        district &&
        settlement_type &&
        settlement ? $emit('step', 2) : Inform()
      "
      color="primary"
      label="Продолжить"
    />
  </q-stepper-navigation>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  location: {
    type: Object,
    default(rawProps) {
      return {
        full_adress: null,
        region: {
          region_type: null,
          region_name: null,
          full_name_region: null,
        },
        settlement: {
          settlement_type: null,
          settlement_name: null,
          full_name_settlement: null,
        },
        district: {
          district: null,
          district_full_name: null,
          district_type: null,
        },
      };
    },
  },
});

const full_adress = ref(props.location?.full_adress || null);
const region = ref(props.location?.region?.full_name_region || null);
const district = ref(props.location?.district.district_full_name || null);
const settlement_type = ref(props.location?.settlement.settlement_type || null);
const settlement = ref(props.location?.settlement.settlement_name || null);
</script>

<style lang="scss" scoped></style>
