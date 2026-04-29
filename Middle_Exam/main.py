import os
from file_manager import list_files, create_folder, move_file
from classifier import classify_file
from renamer import get_new_name
from preview import generate_preview
from duplicate import find_duplicates


def organize(folder):
    files = list_files(folder)

    print("\n[미리보기]")
    preview = generate_preview(files, classify_file, get_new_name)

    for p in preview:
        print(f"{p['original']} -> ({p['category']}) -> {p['new_name']}")

    confirm = input("\n정리 실행? (y/n): ")
    if confirm.lower() != 'y':
        return

    for p in preview:
        category_folder = create_folder(folder, p['category'])
        move_file(folder, category_folder, p['original'], p['new_name'])

    print("\n정리 완료!")


def check_duplicates(folder):
    dups = find_duplicates(folder)
    if not dups:
        print("중복 파일 없음")
    else:
        print("중복 파일:")
        for d in dups:
            print(d)


if __name__ == "__main__":
    folder = input("정리할 폴더 경로 입력: ")

    if not os.path.exists(folder):
        print("폴더가 존재하지 않습니다")
    else:
        check_duplicates(folder)
        organize(folder)
