export function validateFormData(email: string, password: string): { isCurrentEmail: boolean, inCurrentPassword: boolean } {
    const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const isCurrentEmail = emailRegex.test(email);
    const inCurrentPassword = password.length >= 8;
    return { isCurrentEmail, inCurrentPassword };
}
