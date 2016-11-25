while [ 1 ]
do
  sleep 5
  if curl 192.168.99.100:500 | grep -q 'I have seen'; then
    echo "Tests passed!"
  else
    echo "Tests failed!"
  fi
done
