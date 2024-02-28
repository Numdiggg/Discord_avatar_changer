
echo "Installing discord.py..."
pip install discord.py==1.7.3
pip install colorama

if [ $? -ne 0 ]; then
    echo -e "\e[91mFailed to install discord.py. Exiting.\e[0m"
    exit $?
fi

echo -e "\e[92mdiscord.py installed successfully.\e[0m"
echo

python Avtar_changer.py

echo
echo "Press any key to exit..."
read -n 1 -s -r
