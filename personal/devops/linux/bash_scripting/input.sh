#! /bin/bash

while true; do
  read -p "Continue (y/N): " is_continue

  if [[ -z ${is_continue} ]]; then
    is_continue="n"
  fi

  case ${is_continue} in
    y|Y)
      echo "User want to continue"
      break
      ;;
    n|N)
      echo "User wants to discontinue"
      break
      ;;
    *)
      echo "Invalid input. Try again."
      ;;
  esac
done

echo "Bye"
