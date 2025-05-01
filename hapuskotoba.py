import os
import json

# Folder data
data_folder = 'data'

# Untuk menyimpan semua kotoba yang sudah pernah muncul
all_seen_kotoba = set()
# Untuk mencatat duplikat yang dihapus
duplicated_records = []

# Baca semua file di folder 'data'
for filename in os.listdir(data_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(data_folder, filename)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                items = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️  Gagal membaca {filename}, mungkin kosong atau formatnya salah. Lewatkan.")
            continue

        filtered_items = []
        for item in items:
            word = item.get('kotoba')
            if word not in all_seen_kotoba:
                filtered_items.append(item)
                all_seen_kotoba.add(word)
            else:
                duplicated_records.append({
                    'kotoba': word,
                    'file': filename
                })

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(filtered_items, f, ensure_ascii=False, indent=2)

# Setelah semua file selesai diproses
if duplicated_records:
    print("\n🗑️  Kotoba duplikat yang telah dihapus:")
    for record in duplicated_records:
        print(f"- {record['kotoba']} (ditemukan di file: {record['file']})")
else:
    print("\n✅ Tidak ada kotoba duplikat ditemukan.")

print('\n✅ Selesai membersihkan semua file di folder "data/".')
