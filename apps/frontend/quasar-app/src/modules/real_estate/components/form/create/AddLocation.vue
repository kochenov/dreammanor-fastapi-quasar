<template>
  <!-- Адрес -->
  <div class="row q-mt-sm wrap q-col-gutter-md">
    <!-- Region -->
    <q-select
      :key="parser.url"
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
    <!--/ Region -->

    <!-- District-->
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
    <!--/ District-->

    <!-- Settlement Type-->
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
    <!--/ Settlement Type-->

    <!-- Settlement-->
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
    <!--/ Settlement-->
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
  <!--/ Полный адрес -->

  <!-- Button Next Step -->
  <q-stepper-navigation>
    <q-btn
      @click="
        full_adress && region && district && settlement_type && settlement
          ? $emit('step', 2)
          : Inform()
      "
      color="primary"
      label="Продолжить"
    />
  </q-stepper-navigation>
  <!--/ Button Next Step -->
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRealEstateParserStore } from "../../../store/parserStore";

onMounted(async () => {
  await loadRegions();
});

const parser = useRealEstateParserStore();
// props
const props = defineProps({
  // Данные локализации
  location: {
    type: Object,
    default(rawProps) {
      return {
        full_adress: null, // полный адрес
        region: {
          region_type: null, // тип региона
          region_name: null, // имя региона
          full_name_region: null, // полное название региона
        },
        settlement: {
          settlement_type: null, // тип поселения
          settlement_name: null, //  название поселения
          full_name_settlement: null, // полное название поселения
        },
        district: {
          district: null, // район название
          district_full_name: null, // полное название
          district_type: null, // тип района
        },
      };
    },
  },
});

/**
 * Основные данные формы для отправки и записи в БД
 *
 */
//TODO Организовать хранение в LocalStorage
const full_adress = ref(props.location?.full_adress || null);
const region = ref(props.location?.region?.full_name_region || null);
const district = ref(props.location?.district.district_full_name || null);
const settlement_type = ref(props.location?.settlement.settlement_type || null);
const settlement = ref(props.location?.settlement.settlement_name || null);

/**
 * Служебные данные: регион
 */

// Добавление нового региона
const modal_form_add_region = ref(false);
const new_region = ref(null); // model новый регион

const save_new_region_to_base = async () => {
  if (new_region.value) {
    await estateStore.addNewRegion({ label: new_region.value });
    new_region.value = null;
    if (!parser.error) {
      loadRegions();
      modal_form_add_region.value = false;
    }
  }
};
// Отображение списка, фильтрация и выбор региона
const region_id_string_options = ref();
const region_id_options = ref(region_id_string_options.value);
const region_id_filter_fn = (val, update) => {
  if (val === "") {
    console.log(region_id_string_options.value);
    update(() => {
      region_id_options.value = region_id_string_options.value;
    });
    return;
  }

  update(() => {
    const needle = val.toLowerCase();
    region_id_options.value = region_id_string_options.value.filter(
      (v) => v.label.toLowerCase().indexOf(needle) > -1
    );
  });
  console.log(region_id_string_options.value);
};

/** Загрузка и обновление регионов */
const load_regions_status = ref(false);
const loadRegions = async () => {
  load_regions_status.value = true;
  //--

  district.value = null;
  settlement_type.value = null;
  settlement.value = null;

  //--
  await parser.getRegions();

  region_id_string_options.value = parser.list_regions;
  console.log(region_id_string_options);
  // if (region_id_string_options.value) {
  //   setTimeout(() => {
  //     load_regions_status.value = false;
  //   }, 60);
  //}
  load_regions_status.value = false;
};
</script>

<style lang="scss" scoped></style>
